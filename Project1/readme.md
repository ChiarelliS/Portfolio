# Project 1 - ETL/ELT pipeline
This is a data engineering project about U.S. companies financial data. The data is fetched daily, when the SEC EDGAR database release new data. The following pipeline is orchestrated using Kestra.
* Company data extraction from API (Python code)
* Creation of a table to store our data in BigQuery
* Upload of the data to the gcs
* Some data transformation using dbt from the cloud
* Creation of some dashboard to get interesting insights from our data


## DATA EXTRACTION 
The first part of the pipeline consists of extracting the data from [SEC API](https://www.sec.gov/search-filings/edgar-application-programming-interfaces).
To access each company data is required the CIK of the company. An updated list of company CIK can be found [here](https://www.sec.gov/files/company_tickers.json).




## DATA TRANSFORMATION AND DATA VISUALIZATION
# - Using dbt to transform our data that is in the datawarehouse in the cloud
# - Creating some interesting dashboards 
