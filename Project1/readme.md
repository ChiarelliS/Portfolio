# Project 1 - ETL/ELT pipeline

# For this project I will
# - extract data from API 
# - load data to a cloud datawarehouse
# - transform data using dbt 

## DATA EXTRACTION AND DATA LOADING
# For this part of the project I will create a kestra pipeline to orchestrate the workflow.
# Creating a Kestra workflow allows me to:
# - schedule the pipeline to run when new data are published (daily, monthly)
# - receive slack messages in case of errors/issues in the workflow
# - load the data directly to GCP using the secret keys feature of kestra to store my SSH keys.

## DATA TRANSFORMATION AND DATA VISUALIZATION
# - Using dbt to transform our data that is in the datawarehouse in the cloud
# - Creating some interesting dashboards 
