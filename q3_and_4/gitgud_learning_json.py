#!/usr/bin/env python3

import flask

app = flask.Flask(__name__)

@app.route('/')
def superbasictest():
    return flask.json.jsonify({ "yoyoyo" : "username-test", "email" : "email-test", "id" : "id-test"})


app.run(port=8000, debug=True)

