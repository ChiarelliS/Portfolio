# Project 1 - ETL/ELT pipeline
This is a **data engineering project** about U.S. companies financial data. 
The data is fetched for the last 5 financial years. The following pipeline is orchestrated using Kestra.
You can get the yml file with the kestra workflow [here](https://github.com/ChiarelliS/Portfolio/blob/main/Project1/workflow.yml). 
* Company data extraction from API (Python code)
* Creation of a table to store our data in BigQuery
* Upload of the data to the gcs
* Some data transformation using dbt from the cloud
* Creation of some dashboard to get interesting insights from our data

NB **to run kestra on your local machine** run in your terminal:\
`docker-compose build` to build the docker-compose image\
`docker-compose up` to create the docker container\
Then you can access kestra UI from `localhost:8080`

**To set up gcp in kestra** store your ssh key in the kv store, then execute the following flows (modify project id, bucket name, dataset value according to your gcp project features): [gcp_kv_flow](https://github.com/ChiarelliS/Portfolio/blob/main/Project1/flows/gcp_kv.yml), [gcp_setup_flow](https://github.com/ChiarelliS/Portfolio/blob/main/Project1/flows/gcp_setup.yml).

The financial data fetched consists of data from companies' annual 10-k forms.
   In this project I am going to extract the total revenue of each company in the last 5 financial years, and I am going to create a csv file containing the following informations about each company:
* Name of the company
* CIK of the company
* Ticker of the company
* Address of the company
* Country of the company's headquarters
* Year of the 10-k
* Total revenue of that year


## DATA EXTRACTION 
The first part of the pipeline consists of extracting the data from [SEC API](https://www.sec.gov/search-filings/edgar-application-programming-interfaces).\
To access each company data is required the CIK of the company. An updated list of company CIK can be found [here](https://www.sec.gov/files/company_tickers.json).\
To extract the data I created a [python script](https://github.com/ChiarelliS/Portfolio/blob/main/Project1/api.py).


## DATA TRANSFORMATION AND DATA VISUALIZATION
# - Using dbt to transform our data that is in the datawarehouse in the cloud
# - Creating some interesting dashboards 
