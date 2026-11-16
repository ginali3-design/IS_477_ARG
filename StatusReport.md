# Milestone 3: Interim Status Report
## Best Cities to Live After College: Comparing Wages, Rent, and Cost of Living Across U.S. Metropolitan Areas

**Course:** IS 477 — Data Management  
**Team:** Aryan Sharma, Gina Li, Ryan Lewis  
**Status as of:** November 16, 2026  
**Project stage:** Preliminary acquisition, cleaning, integration, and quality assessment; final validation and visualization pending

## 1. Project Overview and Current Status

Our project examines which U.S. metropolitan areas offer a favorable financial environment for recent college graduates by comparing median annual wages, median monthly gross rent, and overall cost of living. We use three complementary 2024 sources: the Bureau of Labor Statistics (BLS) Occupational Employment and Wage Statistics, the U.S. Census Bureau's American Community Survey (ACS), and PlainCost's compilation of Bureau of Economic Analysis (BEA) Regional Price Parities. Our questions concern adjusted wages, rent affordability, and relationships between salaries and living costs.

Our [project plan](ProjectPlan.md) proposed cleaning the three datasets and linking them through CBSA identifiers. **Work began later than scheduled.** On November 16, we collected the downloads and created cleaned files, a preliminary integration, and quality-check artifacts. Validation, automation, and visualization remain incomplete.

## 2. Task-by-Task Progress and Repository Artifacts

### Project planning and data acquisition

The [ProjectPlan.md](ProjectPlan.md) was completed for Milestone 2, including research questions, three candidate sources, roles, constraints, and an initial schedule. For the current milestone, the source downloads used were: the 2024 ACS **1-year** table B25064 (rather than the incompatible 2023 ACS 5-year export initially considered); the May 2024 BLS metropolitan OEWS ZIP; and a 2024 PlainCost/BEA regional-price-parity CSV. The team should place these original downloads under `data/raw/` before its release; they are **not included in the current cleaned-artifact package**. Acquisition is not automated yet.

### Data quality assessment and cleaning

The preliminary source-specific cleaning is implemented in [clean_sources.py](scripts/clean_sources.py). The Census cleaner extracts metro records, retains median gross rent (`B25064_001E`) and its margin of error, and removes the metadata description row. The BLS cleaner selects cross-industry, all-occupation records and retains **median** annual wage, not mean wage. The PlainCost cleaner selects 2024 metropolitan records, excludes state-level records, and keeps the overall Regional Price Parity index. All three outputs use five-character CBSA codes and numeric measures:

- [Cleaned Census rent data](data/clean/rent_2024_clean.csv): **393** metropolitan records.
- [Cleaned BLS wage data](data/clean/wages_2024_clean.csv): **393** metropolitan records.
- [Cleaned PlainCost index](data/clean/cost_of_living_2024_clean.csv): **387** metropolitan records.

The [preliminary quality summary](reports/data_quality_summary.json) reports no duplicate CBSA codes or missing required fields among retained rows, and the cleaned files each contain 2024 data. These results establish structural consistency, **not full source accuracy**: suppressed and invalid entries are filtered out, and a sample of values still needs manual comparison to the publishers' original tables. Source-level exclusion counts still need documentation.

### Integration, post-integration checks, and preliminary analysis

The [integration script](scripts/integrate_and_assess.py) performs an **inner join on CBSA code**, calculates preliminary affordability measures, and writes quality outputs. It produced [387 matched metropolitan areas](reports/merged_metros_2024.csv), representing approximately **98.5%** of the 393 distinct CBSA codes observed across the three cleaned sources. Six codes occur in the Census and BLS files but not PlainCost; they are listed in [unmatched_metro_codes.csv](reports/unmatched_metro_codes.csv). We left those records unmatched instead of fabricating price-parity values.

The merged file calculates `12 × monthly median gross rent ÷ median annual wage × 100` as a descriptive annual-rent-to-wage ratio and `median annual wage ÷ (RPP index / 100)` as a purchasing-power-adjusted wage proxy. We have **not** selected the final 20–30 metros, fully validated boundaries, or created final charts. Overall RPP already includes housing, so rent will not be deducted again from adjusted wages.

### Documentation, workflow, and visualization

A [working README](README.md) records file meanings, calculations, limitations, source attribution, and how to execute the two current scripts using locally supplied raw files. The current pipeline does **not** run end-to-end in one command. Acquisition/checksums, orchestration, software requirements, a data dictionary, and metadata remain pending. Data visualization and a final report have not yet been completed.

## 3. Updated Timeline

The original October and early-November milestones were missed. Dates below are revised targets, **not claims of completed work**. Confirm the final deadline in Canvas.

| Task | Original target | Status on Nov. 16 | Revised target | Lead |
|---|---|---|---|---|
| Finalize project plan | Oct. 14 | Complete | Complete | All |
| Acquire and preserve three raw datasets | Oct. 18 | Downloaded; raw repository uploads pending | Nov. 17 | Aryan / Gina / Ryan by source |
| Assess and clean source datasets | Oct. 23 | Preliminary cleaning complete; source spot-checks pending | Nov. 18 | Each source owner |
| Integrate by CBSA | Oct. 30 | Preliminary 387-row join complete; geographic review pending | Nov. 19 | All |
| Pre/post-integration quality review | Nov. 4 | Basic counts and checks complete; fuller accuracy review pending | Nov. 20 | All |
| Affordability calculations and city selection | Nov. 13 | Two exploratory metrics calculated; shortlist pending | Nov. 21 | Aryan / Ryan; all select cities |
| Visualizations | Nov. 20 | Not started | Nov. 24 | Gina with team review |
| Reproducible workflow and documentation | Nov. 25 | Two scripts and interim README exist; automation pending | Dec. 1 | All |
| Final report, testing, and release | Nov. 30 | Not started | Dec. 7 | All |

## 4. Changes to the Original Plan

Our research questions and three-source approach remain unchanged. The most significant revision is the schedule: because acquisition and cleaning began later than expected, we are prioritizing a verifiable data-curation chain over early visual design. We also changed the *working integration scope*: rather than selecting 20–30 metros before inspecting coverage, we first joined every available metropolitan record (387 shared CBSAs) and will select a balanced 20–30-city comparison set afterward. This lets us assess coverage before selecting cities.

We clarified two methodological choices: BLS **all-occupation median annual wages** must not be described as graduate starting salaries, and the RPP-adjusted wage calculation must not double-count housing. We also prioritized automation and explicit quality reporting. **Milestone 2 instructor feedback has not been provided here; the team must review that feedback and update [ProjectPlan.md](ProjectPlan.md) accordingly before submitting this release.** We will not claim to have implemented feedback we have not reviewed.

## 5. Challenges, Responses, and Next Steps

**Source-version confusion.** Census offers multiple years and one-year/five-year survey products, which are not interchangeable with our proposed 2024 cross-source comparison. We resolved this by using 2024 ACS 1-year B25064 and retaining the survey year in the cleaned output. **Metro matching.** Despite common CBSA codes, six areas do not appear in the PlainCost metro extract. The inner join excludes them transparently, while the unmatched-code log preserves an audit trail. We still need to verify whether CBSA boundary vintages are equivalent across the sources; a matching code alone does not prove perfectly aligned geographic boundaries.

**Data meaning and uncertainty.** The ACS figure is median gross rent for renter-occupied units, whereas the BLS figure is a median wage across occupations; the two do not describe the same individuals. We will present the ratio as a geographic indicator rather than an individual's rent burden. ACS margins of error remain in the cleaned rent file but are not yet propagated into computed rankings. **Reproducibility.** Today's scripts accept downloaded input files and use relative output paths, but the current workflow still requires manual downloads and individual script execution. We plan to add acquisition documentation/checksums, an orchestrator, and a clean-clone test. We will check data redistribution and attribution terms.

Our immediate next steps are to commit the raw source files and current artifacts, validate example observations against each publisher, review any Milestone 2 feedback, and choose 20–30 comparison metros. Then we will complete visualizations and automate the end-to-end workflow. Each person will review their source and commit a personal contribution statement before the **status-report** release is created.

## 6. Individual Contribution Section

**Aryan Sharma:** For this milestone, Aryan was responsible for the Bureau of Labor Statistics (BLS) wage dataset. His contributions included reviewing the 2024 metropolitan-area wage data, checking the cleaned records for consistency, and examining how wage information could be integrated with the other datasets using CBSA codes. He also helped review the affordability calculations and identify remaining data-quality considerations.

**Gina Li:** For this milestone, Gina focused on the U.S. Census Bureau's 2024 American Community Survey rent dataset. Her contributions included locating and downloading the correct ACS 1-Year median gross rent data, checking the geographic coverage, and preparing the dataset for the cleaning process. She also contributed to organizing the project's interim deliverables and documenting progress for the status report.

**Ryan Lewis:** For this milestone, Ryan was responsible for the 2024 cost-of-living dataset sourced from PlainCost and the Bureau of Economic Analysis. His contributions included reviewing the regional price parity data, checking the geographic identifiers, and identifying how the cost-of-living index could be used to calculate adjusted annual wages. He also contributed to reviewing integration results and documenting the remaining steps for the project.
