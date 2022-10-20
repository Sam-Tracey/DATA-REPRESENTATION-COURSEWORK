'''
Author:     Sam Tracey.
Course:     Data Representation.
Date:       October 13th 2022.
Task:       Write a program that retrieves the dataset for the "exchequer account (historical series) from the CSO, and stores it into a file called "cso.json.

'''

# Import Necessary Libraries.
import requests
import json


# Define the cso standard parts of the API address.
urlBeginning = 'https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/'
urlEnd = '/JSON-stat/2.0/en'


# Read all from CSO API to json.
def getAll(dataset):
    url = urlBeginning + dataset + urlEnd
    response = requests.get(url)
    return response.json()


# Write retrieved data to json file.
def writeToJson(dataset):
    with open('cso.json', 'w') as outfile:
        json.dump(getAll(dataset), outfile)


# Call the function to write the data to json.
if __name__ == "__main__":
    writeToJson("FIQ02")




