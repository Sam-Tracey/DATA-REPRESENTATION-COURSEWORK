'''
Author:     Sam Tracey.
Course:     Data Representation.
Date:       October 22nd 2022.
Task:       Using api keys to convert htlm to pdf using www.htmltopdf.app

'''

import requests
import urllib.parse
from config import config as cfg

targetUrl = "https://en.wikipedia.org/wiki/Main_Page"

apiKey = cfg["htmltopdfkey"]
apiUrl = "https://api.html2pdf.app/v1/generate"

params = {'url': targetUrl, 'apiKey': apiKey}
parsedparams = urllib.parse.urlencode(params)

requestUrl = apiUrl + "?" + parsedparams

response = requests.get(requestUrl)

print (response.status_code)
result = response.content

with open("wikipedia.pdf", "wb") as file:
    file.write(result)

