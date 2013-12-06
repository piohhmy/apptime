from flask import Flask
import flask
import json
import logging
import os
import uuid
from flask_helper import crossdomain
from apptime import mongo_repo

app = Flask(__name__, static_url_path='')
logging.basicConfig(level=logging.INFO)

@app.route('/')
@crossdomain(origin='*')
def root():
  return app.send_static_file('index.html')


@app.route("/apptime/user/<username>/apps/usage", methods=["GET", "POST"])
@crossdomain(origin='*')
def usage(username):
    if flask.request.method == 'GET':
        return flask.jsonify(**{ "usage": [
                       {"category": "Game", "apps" :
                              mongo_repo.find_rec(username, "Game")
                       },
                       {"category": "Social", "apps" : 
                              mongo_repo.find_rec(username, "Social")
                       },
                       {"category": "Other", "apps" : 
                              mongo_repo.find_rec(username, "Other")
                       }
                       ]
        })
    if flask.request.method == 'POST':
        logging.info("Received %s", flask.request.data)
        cat = categorize(flask.request.get_json(force=True))
        mongo_repo.insert(username, cat, flask.request.get_json(force=True))
        return flask.jsonify(**{})

@app.route("/apptime/device", methods=["POST"])
@crossdomain(origin='*')
def device():
    data = flask.request.get_json(force=True)
    logging.info("Registering new device for %s", data["name"])
    return flask.jsonify(**{"id":str(uuid.uuid4())})

@app.route("/apptime/user/<username>/devices", methods=["GET"])
@crossdomain(origin='*')
def user_devices(username):
    return flask.jsonify(**{'devices':[{'device_name': 'Galaxy Nexus',  'id': '123'}]})

@app.route("/apptime/users", methods=["GET"])
@crossdomain(origin='*')
def users():
    return flask.jsonify(**{'users':[{'name': 'Tommy'}, {'name': 'Sandy'}]})

def categorize(data):
    if data["name"] in ["Super Mario Brothers", "Candy Crush"]:
        return "Game"
    elif data["name"] in ["Facebook", "Twitter", "Snapchat"]:
        return "Social"
    else:
        return "Other"
    
def start_server():
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    app.debug = True

if __name__ == "__main__":
    start_server()
