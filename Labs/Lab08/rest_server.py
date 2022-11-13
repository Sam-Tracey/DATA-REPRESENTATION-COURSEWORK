'''
Author:     Sam Tracey.
Course:     Data Representation.
Date:       November 13th 2022.
Task:       Create an application server that will implement a RESTful API.
            The API should allow a user to perform CRUD operations on an entity (eg car sales)
            Test it using CURL.

            The API should be able to:
            - Create a new entity
            - Read an entity
            - Update an entity
            - Delete an entity

            The car entities should have the following properties:
            - Make
            - Model
            - Year
            - Price
            - ID

'''

# Importing the required modules.
from flask import Flask, jsonify, request, url_for, redirect, abort

# Creating the Flask application.
app = Flask(__name__, static_url_path="", static_folder="staticpages")


cars = [{"id": 1, "make": "Ford", "model": "Fiesta", "year": 2018, "price": 10000},
        {"id": 2, "make": "Skoda", "model": "Octavia", "year": 2019, "price": 20000},
        {"id": 3, "make": "Volvo", "model": "S40", "year": 2020, "price": 22000},
        {"id": 4, "make": "Kia", "model": "Ceed", "year": 2021, "price": 40000},
        {"id": 5, "make": "Ford", "model": "F150", "year": 2022, "price": 50000}]
nextId = 6       

@app.route("/")
def index():
    return "hello"

# Get all cars curl: curl http://127.0.0.1:5000/cars
@app.route('/cars', methods=['GET'])
def getAll():
    return jsonify(cars)

# Find by ID
@app.route('/cars/<int:id>')
def findById(id):
    foundcars = list(filter(lambda t: t['id'] == id, cars))
    # If nothing was found, return a 404 error otherwise return the first element.
    if len(foundcars) == 0:
        return jsonify({}), 204
    return jsonify(foundcars[0])

# Create a new car
# Curl: curl -X POST -H "content-type:application/json" -d "{\"make\":\"test\", \"model\":\"some car\", \"year\":2017, \"price\":5000}" http://127.0.0.1:5000/cars
@app.route('/cars', methods=['POST'])
def create():
    # Pull in nextId variable from global scope.
    global nextId
    # Check if the request is in JSON format.
    if not request.json:
        abort(400)
    
    # Create a new car object.
    car = {"id": nextId, "make": request.json["make"], "model": request.json["model"], "year": request.json["year"], "price": request.json["price"]}
    cars.append(car)
    nextId += 1
    
    return jsonify(car)

# Update a car
# curl -X PUT -H "content-type:application/json" -d "{\"make\":\"New test\", \"model\":\"some car\", \"year\":2017, \"price\":999}" http://127.0.0.1:5000/cars/1
@app.route('/cars/<int:id>', methods=['PUT'])
def update(id):
    foundcars = list(filter(lambda t: t['id'] == id, cars))
    # Error handling.
    if len(foundcars) == 0:
        return jsonify({}), 404
    if not request.json:
        abort(400)
    currentcar = foundcars[0]
    # Check which fields are being updated.
    if 'make' in request.json:
        currentcar['make'] = request.json['make']
    if 'model' in request.json:
        currentcar['model'] = request.json['model']
    if 'year' in request.json:
        currentcar['year'] = request.json['year']
    if 'price' in request.json:
        currentcar['price'] = request.json['price']
    return jsonify(currentcar)

    

# Delete a car
# curl  -X DELETE http://127.0.0.1:5000/cars/1
@app.route('/cars/<int:id>', methods=['DELETE'])
def delete(id):
    foundcars = list(filter(lambda t: t['id'] == id, cars))
    if len(foundcars) == 0:
        return jsonify({}), 404
    cars.remove(foundcars[0])
    return jsonify({"done": True})


if __name__ == "__main__":
    print("Starting app...")
    app.run(debug=True)