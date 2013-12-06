from flask import Flask
import flask
import json
import logging
import os
import pymongo

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route("/apptime/devices/<id>/usage", methods=["GET", "POST"])

client = MongoClient('mongodb://heroku_app20099764:94dacdf5097e43d72c784cdb50f0186a@ds053698.mongolab.com:53698/heroku_app20099764')
db = client.get_default_database()
collection = db.apptime_db

def hello(id):
    return flask.jsonify(**{ "usage": [
                   {"Appname": "Super mario brothers"},
                   {"Appname": "Frogger"}
                   ]
    })


def start_server():
    port = int(os.environ.get('PORT', 5000))
    app.debug = True
    app.run(host='0.0.0.0', port=port)
	
if __name__ == "__main__":
    start_server()
