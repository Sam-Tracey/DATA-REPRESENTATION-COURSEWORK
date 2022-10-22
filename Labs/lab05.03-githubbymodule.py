'''
Author:     Sam Tracey.
Course:     Data Representation.
Date:       October 22nd 2022.
Task:       Lab 5.03 using packages

'''

from github import Github
from config import config as cfg
import requests

apikey=cfg["githubkey"]


# g = Github(apikey)
# for repo in g.get_user().get_repos():
#     print(repo.name)

g = Github(apikey)
repo = g.get_repo("Sam-Tracey/aprivateone")
# print(repo.name)

fileInfo = repo.get_contents("test.txt")
urlOfFile = fileInfo.download_url
print (urlOfFile)

response = requests.get(urlOfFile)
contentOfFile = response.text
print (contentOfFile)

newContents = contentOfFile + " more stuff \n"

gitHubResponse=repo.update_file(fileInfo.path,"updated by prog",newContents,fileInfo.sha)
print (gitHubResponse)