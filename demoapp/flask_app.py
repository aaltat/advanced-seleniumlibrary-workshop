from flask import Flask, render_template, request, send_from_directory
from time import sleep
import logging
app = Flask(__name__)

app.logger.setLevel(logging.DEBUG)

def rf(name):
    content = ""
    with open(name,'r') as buf:
        content = buf.read()
    return content

@app.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

@app.route("/api.js")
def api():
    return  send_from_directory("html", "api.js")

@app.route("/bindings.js")
def bindings():
    return  send_from_directory("html", "bindings.js")

@app.route("/code.js")
def code():
    return  send_from_directory("html", "code.js")

@app.route("/fetch")
def fetch():
    sleep(4)
    return  send_from_directory("html", "fetch.json")


@app.route('/<path:path>')
def send_js(path):
    return send_from_directory('html', path)
