'''
Author:     Sam Tracey.
Course:     Data Representation.
Date:       October 22nd 2022.
Task:       Using api keys to access Github Repository

'''

import requests
import json
from config import config as cfg


filename = "sam-repos.json"
apikey = cfg["githubkey"]

url = "https://api.github.com/repos/Sam-Tracey/aprivateone"

response = requests.get(url, auth = ('token', apikey))
print (response.status_code)

with open(filename, "w") as f:
    json.dump(response.json(), f, indent=4)
