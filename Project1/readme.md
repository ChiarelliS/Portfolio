## Automated Financial Data Pipeline from SEC Filings to Cloud Warehouse

**Description:**


This project focuses on building an automated data engineering pipeline to extract, load, and transform financial data submitted by companies to the U.S. Securities and Exchange Commission (SEC).\
The pipeline retrieves company information and financial statements—specifically total yearly revenue for the past five years—using the SEC’s EDGAR API.\
The extracted data is loaded into cloud storage (GCS) and to cloud data warehouse (BigQuery), where it is cleaned, structured, and transformed using dbt Cloud to create analytics-ready tables.\
The entire workflow is orchestrated using Kestra to ensure scalability, automation, and reliability.


***


NB **to run kestra on your local machine** run in your terminal:\
`docker-compose build` to build the docker-compose image\
`docker-compose up` to create the docker container\
Then you can access kestra UI from `localhost:8080`

**To set up gcp in kestra**:
* open your working namespace in kestra
* store your ssh key in the kv store
* then execute the following flows (modify project id, bucket name, dataset value according to your gcp project features): [gcp_kv_flow](https://github.com/ChiarelliS/Portfolio/blob/main/Project1/flows/gcp_kv.yml), [gcp_setup_flow](https://github.com/ChiarelliS/Portfolio/blob/main/Project1/flows/gcp_setup.yml).

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


# TODO
1. WATCH DBT VIDEOS AND WORK WITH DBT
2. ADD DBT WORKFLOW
3. ORCHESTRATE THE WORKFLOWS
4. CREATE DASHBOARDS AND PUBLISH DOES HERE



## DATA TRANSFORMATION AND DATA VISUALIZATION
# - Using dbt to transform our data that is in the datawarehouse in the cloud
# - Creating some interesting dashboards 
