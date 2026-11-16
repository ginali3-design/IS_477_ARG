"""Assess cleaned datasets and merge matched metro rows on CBSA code.
Usage: python scripts/integrate_and_assess.py <clean_dir> <output_dir>
"""
import csv,json,sys
from pathlib import Path

def read(path):
    with open(path,encoding='utf-8',newline='') as f:return list(csv.DictReader(f))
def save(path,rows,headers):
    with open(path,'w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=headers);w.writeheader();w.writerows(rows)
def main():
    folder,out=map(Path,sys.argv[1:3]);out.mkdir(parents=True,exist_ok=True)
    paths={'rent':folder/'rent_2024_clean.csv','wages':folder/'wages_2024_clean.csv','rpp':folder/'cost_of_living_2024_clean.csv'}
    source={k:read(p) for k,p in paths.items()}
    indexed={k:{r['cbsa_code']:r for r in rows} for k,rows in source.items()}
    sets={k:set(d) for k,d in indexed.items()};common=set.intersection(*sets.values());union=set.union(*sets.values())
    rows=[]
    for code in sorted(common):
        rent,wage,rpp=(indexed['rent'][code],indexed['wages'][code],indexed['rpp'][code])
        monthly=float(rent['median_gross_rent_monthly_usd']);annual=float(wage['median_annual_wage_usd']);index=float(rpp['rpp_overall_index'])
        rows.append({'cbsa_code':code,'metro_name':rent['metro_name_acs'],'median_annual_wage_usd':int(annual),'median_gross_rent_monthly_usd':int(monthly),'rpp_overall_index':index,'annual_rent_pct_median_wage':round(12*monthly/annual*100,2),'rpp_adjusted_median_wage_usd':round(annual/(index/100),2),'year':2024})
    headers=list(rows[0]) if rows else ['cbsa_code']
    save(out/'merged_metros_2024.csv',rows,headers)
    excluded=[{'cbsa_code':code,'in_rent':int(code in sets['rent']),'in_wages':int(code in sets['wages']),'in_rpp':int(code in sets['rpp'])} for code in sorted(union-common)]
    save(out/'unmatched_metro_codes.csv',excluded,['cbsa_code','in_rent','in_wages','in_rpp'])
    report={'cleaned_record_counts':{k:len(v) for k,v in source.items()},'duplicate_cbsa_count':{k:len(v)-len(sets[k]) for k,v in source.items()},'missing_required_values':{k:sum(any(not row.get(c) for c in row if c!='source') for row in v) for k,v in source.items()},'matched_cbsa_count':len(common),'union_cbsa_count':len(union),'unmatched_cbsa_count':len(excluded),'unmatched_by_dataset':{k:len(union-sets[k]) for k in sets},'years_found':{k:sorted({r['year'] for r in v}) for k,v in source.items()},'notes':['All matched files use 2024 and a standardized five-digit CBSA code.','CBSA matches establish an identifier join; metro boundary equivalence and source concepts should still be reviewed.','Median annual wages across all occupations are not entry-level graduate salaries.','RPP is an index with U.S. average 100, not a household budget; housing is already incorporated in overall RPP.','ACS margins of error are retained in rent source, but not propagated into the exploratory calculated ratios.','Accuracy cannot be guaranteed by schema checks alone; verify selected rows against source publications.']}
    (out/'data_quality_summary.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    print(json.dumps(report,indent=2))
if __name__=='__main__':
    if len(sys.argv)!=3:raise SystemExit('Usage: python scripts/integrate_and_assess.py <clean_dir> <output_dir>')
    main()
