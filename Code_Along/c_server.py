from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World"

@app.route('/datainquery', methods=['GET'])
def inquery():
    queryargs = {
        "firstname" : request.args["firstname"],
        "age" : request.args["age"]
    }
    return jsonify(queryargs)


@app.route('/dataasjson', methods=['POST'])
def asjson():
    book = {
        "title" : request.json["title"],
        "author" : request.json["author"],
        "price" : request.json["price"],
    }
    # put the book into a database
    
    print(book)
    return jsonify(book)

if __name__ == '__main__':
    app.run(debug = True)