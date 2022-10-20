'''
Author:     Sam Tracey.
Course:     Data Representation.
Date:       October 13th 2022.
Task:       Code along Week 4 - Extract data from https://api.valoff.ie

'''
import requests
import json
import urllib.parse

# Connect to the VALOFF API
url = 'https://api.valoff.ie/api/Property/GetProperties'

# Parameterize URL.
parametersDict = {
    "Download":"false",
    "Format":"json",
    "CategorySelected":"OFFICE",
    "LocalAuthority":"WICKLOW COUNTY COUNCIL",
    "Fields":"LocalAuthority,Category,AreaPerFloor,NavTotal,CarPark,PropertyNumber,IG,Use,FloorUse,Address,PublicationDate"
}


def getAll():
    parameters = urllib.parse.urlencode(parametersDict)
    # print(parameters) -- Used to test parameter passing.
    # Get the data
    fullurl = url + "?" + parameters
    response = requests.get(fullurl)
    
    # Return the data
    return response.json()
    
    

if __name__ == "__main__":
    with open('week4_valoff.json', 'w') as outfile:
        json.dump(getAll(), outfile)