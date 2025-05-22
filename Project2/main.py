import requests
import xml.etree.ElementTree as ET 
import json
import os
import dlt
from dlt.sources.helpers.rest_client import RESTClient


os.environ["DESTINATION__BIGQUERY__CREDENTIALS"] = os.environ.get("SERVICE_ACCOUNT_KEY")


url_catalogue = "https://ec.europa.eu/eurostat/api/dissemination/catalogue/toc/xml"

file_name = 'eurostat_db.xml'

dataset_name = 'Industry'

country_list = ["DE", "FR", "IT"]

query_params = {
    "format": "JSON",
    "lang" : "EN",
    "indic_bt": "PROD",    # Production
    "nace_r2": "D",        # Energy sector
    "s_adj": "SA",  
    "sinceTimePeriod" : "2024",
    "geo" : ""
}

# define new dlt pipeline
pipeline = dlt.pipeline(
    pipeline_name='prod_data',
    destination='bigquery', # <--- to run pipeline in production
    dataset_name='eurostat_prod'
)

def extract(url, file_name):
    
    response = requests.get(url)

    with open(file_name, 'wb') as f:
        f.write(response.content)


def parse_xml(xmlfile, dataset_name):

    tree = ET.parse(xmlfile) 
    
    root = tree.getroot() 

    table_codes = []
    # Loop through all branches
    for branch in root.findall('.//{*}branch'):
        titles = branch.findall('{*}title')
        for title in titles:
            if title.text == dataset_name:
                # Now get all dataset leaf codes under this branch
                for code in branch.findall('.//{*}leaf[@type="dataset"]/{*}code'):
                    table_codes.append(code.text)
    return(table_codes)

def make_eu_prod_resource(query_params, df_code):
    @dlt.resource(name=f"prod_{df_code}", write_disposition="replace")
    def eu_prod():
        client = RESTClient(base_url="https://ec.europa.eu/eurostat/")
        endpoint = f"api/dissemination/statistics/1.0/data/{df_code}"
        response = client.get(endpoint, params=query_params)
        data = response.json()
        yield data

    return eu_prod

def main(url_catalogue, file_name, dataset_name):
    extract(url_catalogue, file_name)
    table_codes = parse_xml(file_name,dataset_name)
    selected_codes = table_codes[:2]
    for country in country_list:
        query_params['geo'] = country
        for code in selected_codes:
            resource = make_eu_prod_resource(query_params, code)
            load_info = pipeline.run(resource, loader_file_format="parquet", write_disposition="replace")
            print(f"Loaded dataset: {code}")
            print(load_info)


if __name__ == '__main__':
    main(url_catalogue,file_name,dataset_name)
