# Milestone 3: Interim Status Report
## Best Cities to Live After College: Comparing Wages, Rent, and Cost of Living Across U.S. Metropolitan Areas

### Project Overview and Current Status

Our project looks at which U.S. metropolitan areas are the most affordable for recent college graduates by comparing median annual wages, monthly rent, and overall cost of living. We are using three datasets from 2024: the Bureau of Labor Statistics (BLS), the U.S. Census Bureau, and PlainCost, which provides data originally from the Bureau of Economic Analysis (BEA). Through this project, we hope to better understand how salaries compare to living expenses and which cities offer the best financial opportunities for recent graduates.

So far, we have gathered all three datasets and completed the initial cleaning process to make sure the data is organized and consistent. We also began combining the datasets using CBSA codes to match metropolitan areas across each source. While we have made progress on preparing and organizing our data, we still need to double-check our results, create visualizations, and finish making our workflow reproducible.

### Task-by-Task Progress

#### Project planning and data acquisition

For Milestone 2, we completed our [ProjectPlan.md](ProjectPlan.md), where we outlined our research questions, selected our three datasets, divided responsibilities among team members, and established a timeline for completing the project. Since then, we have started collecting the data needed for our analysis. We gathered the 2024 American Community Survey (ACS) median gross rent data, the May 2024 Bureau of Labor Statistics (BLS) wage data, and the 2024 PlainCost cost-of-living data. We made sure to use data from the same year to keep our comparisons consistent. We have downloaded all three datasets and plan to upload the original files to the data/raw/ folder in our GitHub repository.

#### Data quality assessment and cleaning

After downloading our three datasets, we began cleaning and organizing the data so they could be combined and compared. We used a Python script, [clean_sources.py](scripts/clean_sources.py), to remove unnecessary information and standardize the formatting across the files. For the Census dataset, we kept the median monthly rent values and their margins of error. For the BLS dataset, we focused on median annual wages across all occupations, and for PlainCost, we kept the overall cost-of-living index for metropolitan areas. We also organized the datasets using five-digit CBSA codes so we could match the same metropolitan areas across all three sources.

After cleaning, our datasets included:

- [Cleaned Census rent data](data/clean/rent_2024_clean.csv): **393** metropolitan records.
- [Cleaned BLS wage data](data/clean/wages_2024_clean.csv): **393** metropolitan records.
- [Cleaned PlainCost index](data/clean/cost_of_living_2024_clean.csv): **387** metropolitan records.

We also completed some initial [quality checks](reports/data_quality_summary.json) to identify missing values, duplicate CBSA codes, and formatting inconsistencies. Based on our quality check results, we did not find any duplicate CBSA codes or missing required values in the cleaned datasets. However, we still need to double-check some of the values against the original sources to make sure our data is accurate. We also plan to document how many records were removed during the cleaning process and why. We also plan to expand our quality assessment by checking the original datasets before cleaning and comparing them with our cleaned and combined results. This will help us better document any missing information, inconsistencies, or other issues addressed during the cleaning process.

#### Combining the Datasets and Initial Analysis

After cleaning our three datasets, we began combining them using a Python [integration script](scripts/integrate_and_assess.py). We used CBSA codes to match the same metropolitan areas across the datasets through an inner join. This resulted in [387 metropolitan areas](reports/merged_metros_2024.csv) with matching information, which represents approximately 98.5% of the 393 areas in our cleaned datasets. We found that six metropolitan areas were missing from the PlainCost dataset, so we decided to exclude them rather than estimate the missing values. We documented these areas in a separate [file](reports/unmatched_metro_codes.csv) to keep track of which locations were excluded.

Once the datasets were combined, we started calculating a few measures to compare affordability across cities. First, we calculated the percentage of annual wages that would go toward rent by multiplying median monthly rent by 12, dividing it by median annual wages, and multiplying by 100. We also adjusted annual wages using the Regional Price Parity (RPP) index to compare how far salaries could go in different metropolitan areas. Since the RPP index already accounts for housing costs, we made sure not to subtract rent again from the adjusted wages.

Although we have completed these initial calculations, we still need to choose the final 20–30 metropolitan areas for our comparison, double-check that geographic boundaries match across the datasets, and create our final charts and visualizations.

#### Documentation and Remaining Work

We have also started documenting our project in our [README.md](README.md) file, which explains our datasets, calculations, data sources, and how to run our current Python scripts. While we have completed the initial cleaning and integration, our workflow still requires us to run the scripts separately and manually download the original datasets. Moving forward, we plan to connect these steps so the entire process can run automatically and be easily repeated by someone else. We also still need to document our software requirements, create a data dictionary, finish our visualizations, and complete our final project report.

### Updated Timeline

Although we started some tasks later than originally planned, we have made progress on collecting, cleaning, and combining our datasets. We adjusted our remaining deadlines to help us stay organized and complete the project by the final submission date. Although the official final project deadline is December 7, our group is aiming to complete the project by November 30 to allow additional time for reviewing and making any final adjustments.

| Task | Original Deadline | Current Status | Updated Deadline | Responsible |
|---|---|---|---|---|
| Finalize Project Plan | Oct. 14 | Completed | Completed | All Members |
| Data Collection | Oct. 18 | Completed Nov. 16 | Completed | All Members |
| Data Cleaning | Oct. 23 | Initial cleaning completed | Nov. 18 | Each Member |
| Data Integration | Oct. 30 | Initial integration completed | Nov. 18 | All Members |
| Data Quality Checks | Nov. 4 | Initial checks completed | Nov. 19 | All Members |
| Data Analysis | Nov. 13 | Initial calculations completed | Nov. 19 | All Members |
| Data Visualization | Nov. 20 | Not started | Nov. 21 | Gina |
| Documentation and Workflow | Nov. 25 | In progress | Nov. 25 | All Members |
| Final Report and Submission | Nov. 30 | Not started | Nov. 30 (internal target) | All Members |

### Changes to the Original Plan

Our overall project goals, research questions, and three datasets have remained the same since Milestone 2. However, we made a few adjustments to our original plan as we started working with the data. One of the main changes was how we decided to select our metropolitan areas. Originally, we planned to compare 20–30 cities, but we decided to first combine all the available data across the three sources. This gave us 387 metropolitan areas with matching information and allowed us to better understand the data before narrowing down our final selection.

We also adjusted our timeline to account for our progress so far and the remaining work. Additionally, we realized that the BLS wage data includes workers across all occupations, not specifically recent college graduates, so we will make sure to acknowledge this limitation when presenting our findings. We also plan to be careful when comparing wages and rent since the cost-of-living index already includes housing costs.

For Milestone 2, we received a 20/20 on our Project Plan, along with comments indicating that there were no issues with our original approach. Because of this, we did not need to make any changes based on the feedback we received. Instead, our adjustments have mainly been based on what we learned while collecting, cleaning, and combining our datasets.

### Challenges, Responses, and Next Steps

One of the first challenges we encountered was making sure we downloaded the correct datasets. For example, the Census website offers several different years and survey types, and we initially downloaded the 2023 ACS 5-Year dataset instead of the 2024 ACS 1-Year dataset. We resolved this by downloading the correct 2024 data so that all three sources would cover the same year.

Another challenge was matching metropolitan areas across the three datasets. Although we used CBSA codes to combine them, we found that six metropolitan areas were missing from the PlainCost dataset. Rather than estimating the missing information, we decided to exclude these areas from our combined dataset. We also documented the excluded locations in [our unmatched metro areas file](reports/unmatched_metro_codes.csv). We still plan to double-check that the metropolitan areas are defined consistently across all three sources.

We also recognized some limitations in our data. The BLS wage information includes workers across all occupations rather than specifically recent college graduates, and the Census rent data represents renter-occupied housing. Because of this, our calculations will provide a general comparison of affordability rather than an exact estimate of what a recent graduate would earn or spend. We also need to complete some additional quality checks and make sure our cleaning and analysis steps can be repeated easily.

Our next steps are to upload our original datasets and supporting files to GitHub, verify our results against the original sources, and select the final 20–30 metropolitan areas for comparison. After that, we plan to create our visualizations, finalize our workflow, and complete our final report.

### Individual Contribution

**Aryan Sharma:** Was responsible for the Bureau of Labor Statistics (BLS) wage dataset. His work for this milestone focused on the wage data and how it could be used to compare salaries across metropolitan areas. His responsibilities also included reviewing the cleaned wage information and helping with the affordability calculations.

**Gina Li:** Focused on the U.S. Census Bureau's 2024 American Community Survey rent dataset. She located and downloaded the correct Census data, checked that it included metropolitan areas, and helped prepare the files for cleaning and integration. She also helped organize the project materials and document the team's progress for this milestone.

**Ryan Lewis:** Was responsible for the PlainCost cost-of-living dataset, which uses information from the Bureau of Economic Analysis (BEA). His work focused on the cost-of-living data and how the regional price parity index could be used to compare salaries across different metropolitan areas. His responsibilities also included reviewing the combined data and identifying the remaining steps for the project.
