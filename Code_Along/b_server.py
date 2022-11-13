from flask import Flask, url_for, redirect

app = Flask(__name__, static_url_path='', static_folder='staticpages') # pointing to the folder where the html files are

@app.route('/')
def index():
    return "<a href="+url_for('getUser')+">getUsers</a>"

@app.route('/user', methods=['GET'])
def getUser():
    return "Hi there "

@app.route('/user', methods=['POST'])
def postUser():
    return "Getting by ID "

@app.route('/invalid', methods=['GET'])
def invalid():
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug = True)