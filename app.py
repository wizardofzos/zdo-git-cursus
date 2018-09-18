# -*- coding: utf-8 -*-
from flask import Flask,request,jsonify,redirect,url_for,make_response
from flask import render_template
from functools import wraps
from flask import Response

import datetime
import random


app = Flask(__name__)

app.debug = True


def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid. Always make sure to add randomness
    to the check, so it's not guessable if validuser or not.
    """
    #TODO random sleep here...
    if username == "test":
        return True
    return False

def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="HTTP Basic Auth Required (not advised)"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated


@app.route('/')
def home():
    return render_template('pages/home.html')

@app.route('/todo')
def todo():
    return render_template('pages/todo.html')


@app.route('/u-<username>')
@requires_auth
def user(username):
    return render_template('pages/user.html', username=username)
@app.route('/<path:path>')
def catch_all(path):
    return render_template('pages/404.html')
