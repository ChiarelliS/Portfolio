import requests
import pandas as pd
import xmltodict
import xml.etree.ElementTree as ET 
import json
from pyjstat import pyjstat

tree = ET.parse('eurostat_db.xml') 
#print(dir(tree)) # to look at the functions for this object
  
# get root element 
root = tree.getroot() 

# ET.dump(tree) # this returns the whole tree

table_codes = []
# Loop through all branches
for branch in root.findall('.//{*}branch'):
    titles = branch.findall('{*}title')
    for title in titles:
        if title.text == "Industry":
            # Now get all dataset leaf codes under this branch
            for code in branch.findall('.//{*}leaf[@type="dataset"]/{*}code'):
                table_codes.append(code.text)

# print(table_codes)

code = 'sts_inpr_m'

json_arr = []

url_dataset = f"https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/sts_inpr_m?format=JSON&sinceTimePeriod=2020-01&geo=BE&geo=BG&geo=CZ&geo=DK&geo=DE&unit=I21&unit=PCH_SM&indic_bt=PRD&lang=en"
response = requests.get(url_dataset)
data = json.loads(response.content)
json_arr.append(data)

# dataset = pd.read_json('data.json')
json_string = json.dumps(response.json())
dataset = pyjstat.Dataset.read(json_string)


df = dataset.write('dataframe')

# Display result
print(df.head())

df.to_csv('file1.csv')

#print(dir(df))
# print(df.values.tolist())

# with open('data.json', 'w') as outfile:
    #json.dump(json_arr, outfile)
# print(json_arr)





  