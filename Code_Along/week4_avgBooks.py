'''
Author:     Sam Tracey.
Course:     Data Representation.
Date:       October 13th 2022.
Task:       Code along Week 4 - APIs Part 2. Get average price using APIs

'''

import week4_APIs as APIs

books = APIs.getAllBooks()

total = 0
count = 0

for book in books:
    # print(book["Title"])
    total = total + book["Price"]
    count = count + 1

average = total / count
print("The average Price is: £", round(average, 2))