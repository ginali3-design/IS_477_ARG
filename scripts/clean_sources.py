"""Clean 2024 ACS B25064, BLS OEWS and PlainCost BEA RPP files.
Usage: python scripts/clean_sources.py <acs.zip> <bls.zip> <plaincost.csv> <output_dir>
Uses Python standard library only; no machine-specific paths.
"""
import csv, io, re, sys, zipfile, xml.etree.ElementTree as ET
from pathlib import Path
from collections import Counter

def write_rows(path, columns, rows):
    with open(path,'w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f, fieldnames=columns); w.writeheader();w.writerows(rows)

def number(s):
    try:
        s=str(s).replace(',','').strip()
        if s in ('','-','**','***','N','(X)','null','#'): return None
        return float(s)
    except (ValueError,TypeError): return None

def clean_acs(path,out):
    with zipfile.ZipFile(path) as z:
        name=next(n for n in z.namelist() if n.endswith('-Data.csv'))
        records=list(csv.DictReader(io.TextIOWrapper(z.open(name),encoding='utf-8-sig')))
    results=[]; skipped=Counter()
    for row in records:
        geoid=(row.get('GEO_ID') or '').strip()
        match=re.fullmatch(r'310M700US(\d{5})',geoid)
        if not match: skipped['non_metro_or_metadata']+=1;continue
        val=number(row.get('B25064_001E'))
        if val is None or val<=0: skipped['invalid_or_suppressed_rent']+=1; continue
        moe=number(row.get('B25064_001M'))
        results.append({'cbsa_code': match.group(1),'metro_name_acs': row['NAME'].strip(), 'median_gross_rent_monthly_usd':int(val), 'rent_moe_usd': int(moe) if moe is not None else '', 'year':2024,'source':'Census ACS 2024 1-year B25064'})
    results.sort(key=lambda x:x['cbsa_code'])
    write_rows(out/'rent_2024_clean.csv',list(results[0]),results)
    return results,dict(skipped)

def extract_bls_rows(z):
    # Read only the occupational total records from the large Excel sheet, using
    # streamed Office Open XML parsing to avoid loading ~150,000 rows into RAM.
    n='{http://schemas.openxmlformats.org/spreadsheetml/2006/main}'
    with z.open('xl/sharedStrings.xml') as f:
        strings=[''.join(t.text or '' for t in e.iter(n+'t')) for event,e in ET.iterparse(f,events=('end',)) if e.tag==n+'si']
    with z.open('xl/worksheets/sheet1.xml') as f:
        for event,e in ET.iterparse(f, events=('end',)):
            if e.tag!=n+'row':continue
            if e.attrib.get('r')=='1': e.clear(); continue
            cols={}
            for c in e.findall(n+'c'):
                col=re.match(r'[A-Z]+',c.attrib['r']).group()
                # Only columns essential to filtering and the output
                if col not in ('A','B','C','E','H','I','AB'):continue
                v=c.find(n+'v'); value=v.text if v is not None else ''
                if c.attrib.get('t')=='s' and value: value=strings[int(value)]
                cols[col]=value
            if cols.get('I')=='00-0000' and cols.get('E')=='000000' and cols.get('H')=='1235':
                yield cols
            e.clear()

def clean_bls(path,out):
    results=[];skipped=Counter()
    with zipfile.ZipFile(path) as z:
        xlsx=next(p for p in z.namelist() if p.endswith('MSA_M2024_dl.xlsx'))
        # Open inner xlsx ZIP from outer BLS ZIP
        with zipfile.ZipFile(io.BytesIO(z.read(xlsx))) as workbook:
            for row in extract_bls_rows(workbook):
                code=str(row.get('A','')).zfill(5)
                if not re.fullmatch(r'\d{5}',code):skipped['invalid_cbsa']+=1;continue
                wage=number(row.get('AB'))
                if wage is None or wage<=0:skipped['invalid_or_suppressed_wage']+=1;continue
                results.append({'cbsa_code':code,'metro_name_bls':row.get('B','').strip(),'median_annual_wage_usd':int(wage),'year':2024,'source':'BLS OEWS May 2024 all occupations'})
    results.sort(key=lambda x:x['cbsa_code'])
    write_rows(out/'wages_2024_clean.csv',list(results[0]),results)
    return results,dict(skipped)

def clean_plaincost(path,out):
    results=[]; skipped=Counter()
    with open(path,encoding='utf-8-sig',newline='') as f:
        reader=csv.DictReader(line for line in f if not line.startswith('#'))
        for row in reader:
            if row.get('geography_type')!='metro':skipped['non_metro']+=1;continue
            if row.get('data_year')!='2024':skipped['other_year']+=1;continue
            code=str(row.get('geography_id','')).strip().zfill(5)
            if not re.fullmatch(r'\d{5}',code):skipped['invalid_cbsa']+=1;continue
            rpp=number(row.get('rpp_all'))
            if rpp is None or rpp<=0:skipped['invalid_rpp']+=1;continue
            results.append({'cbsa_code':code,'metro_name_plaincost':row['name'].strip(),'rpp_overall_index':round(rpp,3),'year':2024,'source':'PlainCost / BEA 2024 RPP'})
    results.sort(key=lambda x:x['cbsa_code'])
    write_rows(out/'cost_of_living_2024_clean.csv',list(results[0]),results)
    return results,dict(skipped)

def main():
    acs,bls,plain,out=map(Path,sys.argv[1:5]);out.mkdir(parents=True,exist_ok=True)
    for title,fun,path in [('Census',clean_acs,acs),('BLS',clean_bls,bls),('PlainCost',clean_plaincost,plain)]:
        rows,issues=fun(path,out)
        codes=[r['cbsa_code'] for r in rows]
        print(title, 'valid rows:',len(rows), 'duplicate CBSA:',len(codes)-len(set(codes)), 'skipped:',issues)

if __name__=='__main__':
    if len(sys.argv)!=5: raise SystemExit('Usage: python scripts/clean_sources.py acs.zip bls.zip plaincost.csv output_dir')
    main()
