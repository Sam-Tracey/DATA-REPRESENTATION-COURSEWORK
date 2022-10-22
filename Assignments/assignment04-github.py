'''
Author:     Sam Tracey.
Course:     Data Representation.
Date:       October 13th 2022.
Task:       Write a program in python using the Github module that will read the lab4.txt file from github "Sam-Tracey/aprivateone repository, 
            the program should then replace all the instances of the text "Andrew" with the name "Sam".
            The program should then commit those changes and push the file back to the repository.

'''


# Import Necessary Libraries.
from github import Github
from config import config as cfg
import requests

apikey=cfg["githubkey"]

# Get the file from github.
g = Github(apikey)
repo = g.get_repo("Sam-Tracey/aprivateone")
fileInfo = repo.get_contents("lab4.txt")
urlOfFile = fileInfo.download_url
response = requests.get(urlOfFile)
contentOfFile = response.text

# Replace the text "Andrew" with "Sam".
newContents = contentOfFile.replace("Andrew", "Sam")

# Commit the changes and push the file back to the repository.
gitHubResponse=repo.update_file(fileInfo.path,"updated by prog",newContents,fileInfo.sha)
print (gitHubResponse)



