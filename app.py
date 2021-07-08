from flask import Flask
from nQueen import *
app= Flask(__name__)

@app.route('/<name>')
def index(name):
    return "<h1>Hello{}".format(name)