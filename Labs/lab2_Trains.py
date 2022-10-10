'''
Author:     Sam Tracey.
Course:     Data Representation.
Date:       October 23rd 2022.
Task:       Write a program that prints the data for all trains in Ireland to the console.
            Use the Irish rail API
            http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML
            to retrieve the data.

'''

import requests
import csv
from xml.dom.minidom import parseString

# An array which stores all the tags we want to retrieve.
retrieveTags=['TrainStatus',
            'TrainLatitude',
            'TrainLongitude',
            'TrainCode',
            'TrainDate',
            'PublicMessage',
            'Direction'
            ]



url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get(url)
doc = parseString(page.content)
# print (doc.toprettyxml()) #output to console comment this out once you know it works
# Store the xml in a file. 
with open("trainxml.xml","w") as xmlfp:
    doc.writexml(xmlfp)

# https://stackoverflow.com/questions/3348460/csv-file-written-with-python-has-blank-lines-between-each-r# adding the newline= '' parameter
with open('week02_train.csv', mode='w', newline='') as train_file:
    train_writer = csv.writer(train_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
    for objTrainPositionsNode in objTrainPositionsNodes:
        #traincodenode = objTrainPositionsNode.getElementsByTagName("TrainCode").item(0)
        #traincode = traincodenode.firstChild.nodeValue.strip()
        # Modified to retrieve train latitudes.
        # trainlatitudenode = objTrainPositionsNode.getElementsByTagName("TrainLatitude").item(0)
        # trainlatitude = trainlatitudenode.firstChild.nodeValue.strip()
        dataList = []
        for retrieveTag in retrieveTags:
            datanode = objTrainPositionsNode.getElementsByTagName(retrieveTag).item(0)
            dataList.append(datanode.firstChild.nodeValue.strip())
        train_writer.writerow(dataList)
    
