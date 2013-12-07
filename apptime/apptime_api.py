from flask import Flask
import flask
import json
import logging
import os
import uuid
import datetime
import requests
import urllib
from flask_helper import crossdomain
from apptime import mongo_repo

app = Flask(__name__, static_url_path='')
logging.basicConfig(level=logging.INFO)

active_curfew =[] 
curfew_time = {}

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
                       }
                       ]
        })
    if flask.request.method == 'POST':
        logging.info("Received %s", flask.request.data)
        cat = categorize(flask.request.get_json(force=True))
        mongo_repo.insert(username, cat, flask.request.get_json(force=True))
        if username in curfew_time:
            if datetime.datetime.now() - curfew_time[username] > datetime.timedelta(seconds=30):
                send_parent_sms(username)
        if username in active_curfew:
            active_curfew.remove(username)
            curfew_time[username] = datetime.datetime.now()
            return flask.jsonify(**{"curfew_expired":True})
        else:
            return flask.jsonify(**{"curfew_expired":False})

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
    return flask.jsonify(**{'users':[{'name': 'Tommy'}, {'name': 'Sally'}]})

@app.route("/apptime/user/<username>/curfew", methods=["POST"])
@crossdomain(origin='*')
def curfew(username):
    active_curfew.append(username)
    return flask.jsonify(**{})

def categorize(data):
    if data["name"] in ["Super Mario Brothers", "Candy Crush", "Shazam"]:
        return "Game"
    elif data["name"] in ["Facebook", "Twitter", "Snapchat", "LinkedIn", "Quora"]:
        return "Social"
    else:
        return "Other"

def send_parent_sms(username):
    msg = "%s is violating their curfew!" % username 
    url = "http://wolverines.devpsite.info:3000/baby_monitor/send_message?%s" % urllib.urlencode({"message": msg})
    requests.post(url)

def start_server():
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    app.debug = True

if __name__ == "__main__":
    start_server()
