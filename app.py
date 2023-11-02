# Minimal Flask app, as per their documentation.
# See https://flask.palletsprojects.com/en/3.0.x/quickstart/#a-minimal-application

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"
