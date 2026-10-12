# Project Plan
## Best Cities to Live After College: Comparing Wages, Rent, and Cost of Living Across U.S. Metropolitan Areas

### Overview
Our project aims to find the best cities for recent college graduates to live in based on salaries, housing costs, and overall cost of living. Since many college graduates consider moving to a new city after graduation, we want to explore which cities offer the best balance between earning a good salary and living affordably.

To do this, we plan to use three datasets from the Bureau of Labor Statistics (BLS), U.S. Census Bureau, and PlainCost, which provides data originally from the Bureau of Economic Analysis (BEA). These datasets will provide information on median annual wages, rent prices, and cost of living in different cities.

We plan to compare around 20–30 major U.S. metropolitan areas by combining the datasets and looking at how salaries compare to living expenses. We will calculate things like how much of a person's salary would go toward rent and how salaries compare after accounting for differences in cost of living. We will then use charts and tables to compare the areas and identify which ones offer the best financial opportunities for recent graduates.

### Team Responsibilities
**Member 1: Aryan Sharma**
- Research and gather salary data from the Bureau of Labor Statistics 
- Clean and organize the salary data
- Help calculate salary and housing affordability comparisons

**Member 2: Gina Li**
- Research and gather housing and rent data from the U.S. Census Bureau
- Clean and organize the housing data
- Help create charts and graphs to compare cities

**Member 3: Ryan Lewis**
- Research and gather cost-of-living data from PlainCost
- Clean and organize the cost-of-living data
- Help analyze the results and identify key findings

**Shared Responsibilities:**
- Develop research questions and plan the project
- Combine the three datasets into one
- Compare cities and interpret the results
- Review each other's work and complete the final report and presentation

### Research or Business Questions

1. Which major U.S. metropolitan areas offer the highest wages after adjusting for cost of living?
2. How much of a person's annual wage would go toward rent in different metropolitan areas?
3. Do metropolitan areas with higher wages also have higher housing costs and overall living expenses?

### Datasets
For our project, we plan to use three datasets that provide information on salaries, housing costs, and overall cost of living across U.S. metropolitan areas. All three datasets contain information from 2024 and will help us compare which areas offer the best financial opportunities for recent college graduates.

1. Occupational Employment and Wage Statistics (OEWS) — Bureau of Labor Statistics (BLS)
- Source: https://www.bls.gov/oes/tables.htm
- Year: 2024
- Data: Annual wages for different occupations across U.S. metropolitan areas
- Purpose: We will focus on median annual wages for all occupations to compare earning potential in different metropolitan areas

2. American Community Survey (ACS) — U.S. Census Bureau
- Source: https://data.census.gov/table/ACSDT1Y2024.B25064
- Year: 2024
- Data: Median monthly gross rent across U.S. metropolitan areas
- Purpose: We will use rent prices to compare housing affordability and calculate annual rent as a percentage of median annual wages

3. Regional Price Parities (RPP) — PlainCost / Bureau of Economic Analysis (BEA)
- Dataset: https://plaincost.com/data
- Original Source: https://www.bea.gov/data/prices-inflation/regional-price-parities-state-and-metro-area
- Year: 2024
- Data: Cost-of-living indexes across U.S. metropolitan areas, including the overall price levels of goods, housing, and services
- Purpose: We will use the overall cost-of-living index to compare how expensive different metropolitan areas are and how far a salary might go in each location. The data comes from BEA and is compiled by PlainCost

### How We Will Combine the Datasets

All three datasets provide information about U.S. metropolitan areas. We plan to use metropolitan-area identification codes (CBSA codes) to match the same locations across the datasets. We will also check that the codes and metropolitan-area boundaries match before combining the data.

Once combined, we will have annual wage, monthly rent, and cost-of-living information for each metropolitan area. We plan to compare around 20–30 major metropolitan areas and calculate how much of an annual salary would go toward rent, as well as how salaries compare after adjusting for differences in cost of living.

We will also check for missing information and differences between the datasets to make sure our comparisons are consistent.

### Timeline 
Our team plans to complete the project in stages, starting with collecting and organizing our datasets and ending with our final analysis and report. We will divide the work among team members while working together on the major steps. We also plan to document our data sources, cleaning steps, and code so that others can repeat our analysis.

| Task | Description | Target Completion | Responsible |
|---|---|---|---|
| Finalize Project Plan | Confirm research questions, datasets, and project approach. | October 14, 2026 | All Members |
| Data Collection | Download the 2024 salary, housing, and cost-of-living datasets and document their sources. | October 18, 2026 | Aryan: BLS salary data; Gina: Census rent data; Ryan: PlainCost data |
| Data Cleaning | Check for missing values, remove unnecessary columns, and organize each dataset. | October 23, 2026 | Aryan: salary data; Gina: rent data; Ryan: cost-of-living data |
| Data Integration | Match metropolitan areas using geographic identifiers and combine the three datasets. | October 30, 2026 | All Members |
| Data Quality Checks | Check the combined data for accuracy, completeness, consistency, and timeliness. | November 4, 2026 | Aryan: salary values; Gina: rent values; Ryan: cost-of-living values |
| Data Analysis | Calculate rent as a percentage of wages, compare purchasing power, and identify patterns across cities. | November 13, 2026 | Aryan: salary and affordability calculations; Ryan: cost-of-living comparisons; Gina: housing comparisons |
| Data Visualization | Create charts and tables comparing metropolitan areas. | November 20, 2026 | Gina: charts and graphs; Aryan: salary comparisons; Ryan: cost-of-living findings |
| Documentation and Reproducibility | Document data sources, cleaning steps, and code. Create a repeatable workflow with instructions for running the project and checking data integrity. | November 25, 2026 | All Members |
| Final Report and Submission | Summarize findings, review the project, test the workflow, and submit the final GitHub release. | November 30, 2026 | All Members |


### Constraints

Some challenges we may face throughout the project include:

- **Data Consistency:** Although all three datasets use 2024 data, they may organize or define metropolitan areas differently. We will need to make sure the locations match before combining them
- **Missing Data:** Some metropolitan areas may not have complete information across all three datasets. We may need to exclude locations with missing information
- **Data Cleaning:** The datasets may contain unnecessary columns, different formats, or inconsistent geographic identifiers that we will need to organize before analysis
- **Data Sources:** Our cost-of-living dataset is compiled by PlainCost using BEA data. We will need to verify the source information and follow any data usage or attribution requirements
- **Limitations of the Data:** Our salary dataset includes wages across all occupations, not just recent college graduates. Also, our comparisons will not account for every expense, such as taxes, student loans, or individual spending habits
- **Cost-of-Living Comparisons:** The overall cost-of-living index already includes housing costs. We will consider this when comparing salaries and rent to avoid counting housing expenses twice.

### Gaps

There are still a few things we need to determine as we move forward:

- **City Selection:** We still need to decide which 20–30 metropolitan areas to include in our analysis
- **Combining the Data:** We need to confirm that the geographic identifiers are compatible across all three datasets and determine the best way to combine them
- **Analysis Methods:** We still need to decide which calculations and comparisons will best answer our research questions
- **Technical Approach:** We will need to determine which tools to use for data cleaning, integration, analysis, and visualization, as well as how to document the steps so our results can be reproduced
- **Project Updates:** We may need to adjust our plan based on challenges we encounter or feedback from our professor

