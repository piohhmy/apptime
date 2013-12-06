from flask import Flask
import flask
import json
import logging
import os

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route("/apptime/devices/<id>/usage", methods=["POST", "GET"])
def hello(id):
    return flask.jsonify(**{ "usage": [
                   {"Appname": "Super mario brothers"},
                   {"Appname": "Frogger"}
                   ]
    })


def start_server():
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

if __name__ == "__main__":
    start_server()
