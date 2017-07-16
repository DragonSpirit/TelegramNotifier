# -*- coding: utf-8 -*-
import flask
from flask import Flask, request
from src.bot import fire_event

app = Flask(__name__)

@app.route('/')
def index():
    return "Simple telegram events notifier"


@app.route('/fire', methods = ['POST'])
def post():
    if request.headers.get('content-type') == 'application/json':
        json = request.json
        if 'message' in json:
            fire_event(json['message'])
            return "Success"
        return flask.abort(400, "Use correct schema")
    else:
        flask.abort(400, "Use correct header")


def init():
    app.run(
        host = "0.0.0.0",
        port = 80
    )