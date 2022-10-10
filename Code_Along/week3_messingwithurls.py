'''
Author:     Sam Tracey.
Course:     Data Representation.
Date:       October 10th 2022.
Task:       Code along Week 3 - Playing around with URLs

'''

import requests
url = 'https://atu.ie'
response = requests.get(url)
print(response.status_code)
