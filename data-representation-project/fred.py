'''
Reading FRED API ( date and value only)for the following data sets into json files:
Unemployment Rate in South Carolina (SCUR)

'''


import requests
import json

# FRED API key
api_key = '735b868f6c19b3ea684013624f617bdc'

# FRED API URL
url = 'https://api.stlouisfed.org/fred/series/observations?series_id='
dataid = 'SCUR'
url_end = '&api_key=' + api_key + '&file_type=json'

# Read date and value only data from FRED API
r = requests.get(url + dataid + url_end)
data = r.json()

# Write only 'date' and 'value' fields to json file
with open('fred.json', 'w') as f:
    for d in data['observations']:
        json.dump({'date': d['date'], 'value': d['value']}, f)
        









        
    












