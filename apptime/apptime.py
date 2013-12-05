from flask import Flask
import flask
import json
import logging
app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route("/apptime/devices/<id>/usage", methods=["POST"])
def hello(id):
    return flask.jsonify(**{ "usage": [
                   {"Appname": "Super mario brothers"},
                   {"Appname": "Frogger"}
                   ]
    })

if __name__ == "__main__":
        app.run()
