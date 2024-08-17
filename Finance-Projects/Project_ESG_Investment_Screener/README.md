# Project ESG_Investment_Screener: Developing a Tool for Evaluating ESG Criteria in Investment Portfolios

## Overview
The "ESG Investment Screener" project focuses on developing a tool that evaluates and screens investments based on specific Environmental, Social, and Governance (ESG) criteria. The primary goal of this project is to create a systematic approach to identifying investments that align with GreenFuture Capital’s ESG values, enabling them to make informed decisions about where to allocate their capital.

## Objective
The main objective of this project is to build a Python-based tool that allows users to filter and evaluate potential investments according to GreenFuture Capital’s ESG criteria. The tool will help users identify companies and assets that meet the firm’s sustainability and ethical standards, thus supporting the integration of ESG criteria into the investment decision-making process.

## Case Scenario

### Client Profile
GreenFuture Capital is an investment firm based in Europe that specializes in sustainable investing. They manage portfolios for institutional investors and high-net-worth individuals who prioritize ESG considerations in their investment strategies. The firm has established a strong reputation for adhering to strict ESG standards in all of their investment decisions.

### Current Challenge
GreenFuture Capital has been facing difficulties in efficiently identifying and evaluating investment opportunities that meet their strict ESG criteria. The current process is manual, time-consuming, and prone to inconsistencies, leading to potential missed opportunities or the inclusion of investments that do not fully align with their clients’ values.

### Project Assignment
GreenFuture Capital has tasked you with developing an ESG investment screening tool that can automate the evaluation process based on their specific ESG criteria. The tool should be capable of aggregating data from various sources, applying these ESG filters, and generating a list of investments that meet the specified criteria. The tool will play a crucial role in streamlining the firm’s investment selection process and ensuring that all chosen investments align with their ESG mandates.

## ESG Criteria for Screening
GreenFuture Capital uses the following specific ESG criteria for screening investments:

1. **Environmental Criteria:**
   - **Carbon Footprint:** Companies must have a carbon intensity (measured in tons of CO2 per million dollars of revenue) below 100.
   - **Renewable Energy Usage:** At least 20% of the company's energy consumption must come from renewable sources.
   - **Waste Management:** Companies must have a clear waste management policy and demonstrate a year-over-year reduction in waste production.

2. **Social Criteria:**
   - **Diversity and Inclusion:** Companies must have at least 30% representation of women on their board of directors.
   - **Labor Practices:** Companies must have a strong track record of labor rights, including no recent violations of labor laws and a commitment to fair wages.
   - **Community Engagement:** Companies must invest at least 2% of their pre-tax earnings in community development programs.

3. **Governance Criteria:**
   - **Board Independence:** At least 50% of the board members must be independent.
   - **Anti-Corruption Policies:** Companies must have clear anti-corruption policies and no history of corruption scandals within the last 5 years.
   - **Executive Compensation:** The ratio of CEO compensation to the median employee salary should not exceed 100:1.

## Expected Deliverable
**ESG Investment Screener Tool:**
Develop a Python-based application or Jupyter notebook that aggregates data from multiple sources and applies the specific ESG filters outlined above to evaluate potential investments. The tool should:
- **Data Aggregation:** Collect and consolidate ESG-related data that corresponds to the specific criteria listed above.
- **Screening Mechanism:** Apply the specified ESG criteria to screen out investments that do not meet the standards.
- **Report Generation:** Produce a report or list of investments that align with the specified ESG criteria, complete with scores or rankings.

## Key Features to Implement:
1. **Data Integration:** Ability to aggregate ESG data from multiple sources, ensuring a comprehensive evaluation based on the specific criteria.
2. **Customizable ESG Criteria:** The tool should allow users to adjust the weight or importance of different ESG factors within the specified criteria.
3. **Screening and Filtering:** Implement logic to filter out investments that do not meet the minimum ESG thresholds for each of the criteria.
4. **Visualization and Reporting:** Generate visualizations and reports summarizing the ESG performance of screened investments, highlighting how they align with the specified criteria.
5. **User-Friendly Interface:** Ensure that the tool is easy to use, with clear instructions and output that is accessible to non-technical users.

## Instructions
To complete the project, you should:
- Identify relevant ESG data sources that provide information on the specific criteria listed (e.g., carbon footprint, diversity metrics, board independence).
- Design a flexible and customizable ESG scoring system based on the specified criteria that allows users to prioritize different factors.
- Implement the screening mechanism to ensure it can efficiently process and filter a large dataset according to the specified ESG criteria.
- Create clear, informative visualizations and reports that summarize the findings and make them actionable for GreenFuture Capital.
- Test the tool with various datasets to ensure its accuracy and reliability.

The final deliverable should be a single Python-based tool (or notebook) that GreenFuture Capital can use to consistently and accurately screen investments according to their specific ESG criteria.
