## :factory: Monthly Industry Data Extraction From Eurostat Database
### **work in progress**


This project aims to create a pipeline to collect industry data from the [Eurostat database](https://ec.europa.eu/eurostat/data/database) each month, clean the data, upload the tables to cloud storage, and query the data to perform some transformations and prepare the tables for BI.


**TECH STACK**


* Python (restAPI data collection with Python library ['dlt'](https://dlthub.com/))
* Terraform (Infrastructure as code)
* [Kestra](https://kestra.io/) (workflow orchestration)
* Google Cloud Storage
* Google Cloud BigQuery
* [dbt](https://hub.getdbt.com/) (Data Build Tool)
  

---


Sources:

https://ec.europa.eu/eurostat/web/user-guides/data-browser/api-data-access/api-detailed-guidelines/api-statistics

https://ec.europa.eu/eurostat/web/user-guides/data-browser/api-data-access/api-getting-started/catalogue-api

https://ec.europa.eu/eurostat/web/main/data/web-services

https://ec.europa.eu/eurostat/data/database#Flags


