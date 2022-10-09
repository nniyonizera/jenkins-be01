from flask import Flask,jsonify
from flask_cors import CORS

app=Flask(__name__)
cors=CORS(app,resources={r"/*":{"origins":"*"}})
@app.route("/")
def index() :
    hotels=(dict(name='hotel 1',body='hotel1 description'),dict(name='hotel 2',body='hotel2 description'),
            dict(name='hotel 3',body='hotel3 description'),dict(name='hotel 4',body='hotel4 description'),dict(name='hotel 5',body='hotel5 description'))
    data_dict=list(hotels)
    return jsonify(data_dict)
def testValue() :
    return 20
