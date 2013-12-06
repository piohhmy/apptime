from flask import Flask
import flask
import json
import logging
import os
import uuid

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route("/apptime/devices/<id>/usage", methods=["GET", "POST"])
def usage(id):
    if flask.request.method == 'GET':
        return flask.jsonify(**{ "usage": [
                       {"appname": "Super mario brothers", "category": "Game"},
                       {"appname": "Frogger", "category": "Game" }
                       ]
        })
    if flask.request.method == 'POST':
        logging.info("Received %s", flask.request.data)
        return flask.jsonify(**{})

@app.route("/apptime/device", methods=["POST"])
def device():
    data = json.loads(json.dumps(flask.request.data))
    #logging.info("Registering new device for %s", data["name"])
    return flask.jsonify(**{"id":str(uuid.uuid4())})

def start_server():
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

if __name__ == "__main__":
    start_server()
