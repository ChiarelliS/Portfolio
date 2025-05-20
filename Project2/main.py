import requests
import pandas as pd
import xmltodict
import xml.etree.ElementTree as ET 
import json

url_catalogue = "https://ec.europa.eu/eurostat/api/dissemination/catalogue/toc/xml"

file_name = 'eurostat_db.xml'

dataset_name = 'Industry'



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



def main():
    extract(url_catalogue, file_name)
    table_codes = parse_xml(file_name,dataset_name)
    json_arr = []
    for code in table_codes:
        url_dataset = f"https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/{code}?format=JSON&lang=EN"
        response = requests.get(url_dataset)
        data = json.loads(response.content)
        json_arr.append(data)
        # with open('data.json', 'a') as outfile:
            # json.dump(json_arr, outfile)
    print(json_arr)




    
 
   

if __name__ == '__main__':
    main()
