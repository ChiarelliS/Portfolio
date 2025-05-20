import os
import dlt
from dlt.sources.helpers.rest_client import RESTClient



# Get the secret
os.environ["DESTINATION__BIGQUERY__CREDENTIALS"] = os.environ.get("SERVICE_ACCOUNT_KEY")

# Define the API resource for eurostat data
@dlt.resource(name="prod", write_disposition="replace")   # <--- The name of the resource (will be used as the table name)
def eu_prod(query_params):
    client = RESTClient(
        base_url="https://ec.europa.eu/eurostat/")

    params = query_params

    endpoint = "api/dissemination/statistics/1.0/data/sts_inpr_m"

    response = client.get(endpoint, params = params)    # <--- API endpoint for retrieving eurostat data
    
    data = response.json()  
    
    yield data   # <--- yield data to manage memory

query_params = {
    "format": "JSON",
    "lang" : "EN",
    "indic_bt": "PROD",    # Production
    "nace_r2": "D",        # Energy sector
    "s_adj": "SA",  
    "sinceTimePeriod" : "2024",
    "geo" : "DE"
}


# define new dlt pipeline
pipeline = dlt.pipeline(
    pipeline_name='prod_data',
    destination='bigquery', # <--- to run pipeline in production
    dataset_name='eurostat_prod',
)

# run the pipeline with the new resource
load_info = pipeline.run(eu_prod(query_params), loader_file_format="parquet", write_disposition="replace")
print(load_info)


# explore loaded data
pipeline.dataset().prod.df()

