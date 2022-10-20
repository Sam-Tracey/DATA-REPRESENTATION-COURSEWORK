'''
Author:     Sam Tracey.
Course:     Data Representation.
Date:       October 13th 2022.
Task:       Code along Week 4 - Import week3_valoff.py and get Area where ValuationReport FloorUSe is HAIR SALON only.

'''
from week4_valoff import getAll
import json

data = getAll()
totalArea = 0
# Get area for all HAIR SALON (FloorUse)
for entry in data:
    valuationReports = entry['ValuationReport']
    if(valuationReports):
        for report in valuationReports:
            if(report['FloorUse'] == 'HAIR SALON'):
                totalArea += report['Area']
print(f'Total Area of Hair Salons is {totalArea}')



    




