'''
Author:     Sam Tracey.
Course:     Data Representation.
Date:       October 13th 2022.
Task:       Code along Week 4 - APIs Part 1

'''

import requests
url = 'http://andrewbeatty1.pythonanywhere.com/books'



# List all books
def getAllBooks():
    response = requests.get(url)
    return response.json()

# List a single book based on ID.
def getBookByID(id):
    geturl = url + "/" + str(id)
    response = requests.get(geturl)
    return response.json()

# Add a book
def addBook(book):
    response = requests.post(url, json=book)
    return response.json()

# Update a book
def updateBook(id, book):
    puturl = url + "/" + str(id)
    response = requests.put(puturl, json=book)
    return response.json()

# Delete a book
def deleteBook(id):
    deleteurl = url + "/" + str(id)
    response = requests.delete(deleteurl)
    return response.json()




if __name__ == "__main__":
    # Test the functions
    # print(getAllBooks())
    print(getBookByID(110))
    # print(addBook({"Author":"J.R.R. Tolkien", "Price": 10.99, "Title":"The Hobbit"}))
    # print(updateBook(110, {"Price": 100}))
    # print(deleteBook(110))