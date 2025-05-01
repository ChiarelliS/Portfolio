## :scroll: Automated Financial Data Pipeline from SEC Filings to Cloud Warehouse

**Description:**


This project focuses on building an **automated data engineering pipeline** to **extract, load, and transform** financial data submitted by companies to the U.S. Securities and Exchange Commission (SEC).


The pipeline retrieves company information and financial statements—specifically total yearly revenue for the past five years—using the SEC’s EDGAR **API**.


The extracted data is loaded into **cloud storage (GCS)** and to **cloud data warehouse (BigQuery)**, where it is cleaned, structured, and transformed using **dbt Cloud** to create analytics-ready tables.


The data extraction and data loading **workflow** is orchestrated using **Kestra** to ensure scalability, automation, and reliability.


***

## 🛠️ Installation Instructions

> **Note:** To run **Kestra** locally, Docker and Docker Compose must be installed on your machine.

### Steps to Run Kestra Locally

1. `docker-compose build` to build the docker-compose image\
2. `docker-compose up` to create the docker container\
3. Then you can access kestra UI from `localhost:8080`

### Steps to set up gcp in Kestra:
1.  open your working namespace in Kestra
2.  store your ssh key in the kv store
3.  then execute the following flows (modify project id, bucket name, dataset value according to your gcp project features): [gcp_kv_flow](https://github.com/ChiarelliS/Portfolio/blob/main/Project1/flows/gcp_kv.yml), [gcp_setup_flow](https://github.com/ChiarelliS/Portfolio/blob/main/Project1/flows/gcp_setup.yml).

### Python API script


Add the [python script](https://github.com/ChiarelliS/Portfolio/blob/main/Project1/api.py) to your Kestra workflow folder and execute the [workflow](https://github.com/ChiarelliS/Portfolio/blob/main/Project1/flow.yaml)

## Data Transformation with dbt


[Here](https://github.com/ChiarelliS/Portfolio/tree/main/Project1/dbt) you can find the models and DAG of the transformation stage.




