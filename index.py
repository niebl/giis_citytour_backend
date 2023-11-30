#!/bin/python

from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route("/")
def index():
    return "TODO: list of accessible routes"
    
@app.get("/")
def get_poi():
    f = open("/templateData/points.json")
    data = json.load(f)
    jsonify(data)
    return "GET JSON"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)