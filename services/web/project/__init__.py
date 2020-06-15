from flask import Flask, jsonify


server = Flask(__name__)


@server.route("/")
def hello_world():
    return jsonify(hello="world")