'''
Author:     Sam Tracey.
Date:       October 21st 2022.
Task:       Retrieve .json data from Fred Economic Data API and store as dataframe.

'''

import pandas as pd
import requests
import json

# Define the fred data table we are interested in extracting.
urlBeginning = 'https://api.stlouisfed.org/fred/series/observations?series_id='
urlEnd = '&api_key=735b868f6c19b3ea684013624f617bdc&file_type=json'
data_id = 'PCU325211325211'

# Write all data to json file.
def getAllasFile(dataset):
    with open('fred.json', 'w') as outfile:
        json.dump(getAll(dataset), outfile)

# Read all data to json.
def getAll(dataset):
    url = urlBeginning + dataset + urlEnd
    response = requests.get(url)
    return response.json()

# Read all data to dataframe.
def getAllasDF(dataset):
    url = urlBeginning + dataset + urlEnd
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame(data['observations'])
    return df

if __name__ == '__main__':
    getAllasFile(data_id)
    df = getAllasDF(data_id)
    print(df)
