'''
Author:     Sam Tracey.
Course:     Data Representation.
Date:       October 3rd 2022.
Task:       Write a program that reads a .json file from the cloud
            https://api.coindesk.com/v1/bpi/currentprice.json
            to retrieve the data.

'''


import requests
import json
url = "https://api.coindesk.com/v1/bpi/currentprice.json"
response = requests.get(url)
data = response.json()
#with open("bitcoindump.json", "w") as fp:
#    json.dump(data, fp)

# Extract the Euro rate from the .json file.
euroobject = data["bpi"]["EUR"]
rate = euroobject["rate"]
print (rate)
