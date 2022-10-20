'''
Author:     Sam Tracey.
Course:     Data Representation.
Date:       October 13th 2022.
Task:       Code along Week 4 - Extract data from cso.ie API from pxstat format.

'''

import requests
import json
import urllib.parse

# Define the cso data table we are interested in extracting.
urlBeginning = 'https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/'
urlEnd = '/JSON-stat/2.0/en'


# Write all data to json file.
def getAllasFile(dataset):
    with open('cso.json', 'w') as outfile:
        json.dump(getAll(dataset), outfile)


# Read all data to json.
def getAll(dataset):
    url = urlBeginning + dataset + urlEnd
    response = requests.get(url)
    return response.json()


def getFormatted(dataset):
    data = getAll(dataset)
    ids = data['id']
    dimensions = data['dimension']
    values = data['value']
    sizes = data['size']
    valueCount = 0
    result = {}

    for dim1 in range(0, sizes[0]):
        currentId = ids[0]
        index = dimensions[currentId]["category"]["index"][dim1]
        label0 = dimensions[currentId]["category"]["label"][index]
        result[label0]={}

        for dim2 in range(0, sizes[1]):
            currentId = ids[1]
            index = dimensions[currentId]["category"]["index"][dim2]
            label1 = dimensions[currentId]["category"]["label"][index]
            result[label0][label1]={}

            for dim3 in range(0, sizes[2]):
                currentId = ids[2]
                index = dimensions[currentId]["category"]["index"][dim3]
                label2 = dimensions[currentId]["category"]["label"][index]
                result[label0][label1][label2]={}

                for dim4 in range(0, sizes[3]):
                    currentId = ids[3]
                    index = dimensions[currentId]["category"]["index"][dim4]
                    label3 = dimensions[currentId]["category"]["label"][index]
                    result[label0][label1][label2][label3]=values[valueCount]

                    valueCount += 1
    
    print(result)
    return result



def getFormattedAsFile(dataset):
    with open('cso_formatted.json', 'w') as outfile:
        json.dump(getFormatted(dataset), outfile)



# Write extracted data to a file.
if __name__ == "__main__":
    getFormattedAsFile("FP001")




