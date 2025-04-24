# Welcome to my Portfolio!
## Here I add some projects that showcase my skills in data engineering / analytics engineering

# Project 1 - ETL/ELT pipeline
This is a data engineering project about U.S. companies financial data. The data is fetched daily, when the SEC EDGAR database release new data. The following pipeline is orchestrated using Kestra.
* Company data extraction from API (Python code)
* Creation of a table to store our data in BigQuery
* Upload of the data to the gcs
* Some data transformation using dbt from the cloud
* Creation of some dashboard to get interesting insights from our data



