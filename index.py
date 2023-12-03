#!/bin/python

from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route("/")
def index():
    return "TODO: list of accessible routes"
    
@app.get("/template-data")
def get_poi():
    f = open("./templateData/points.json")
    data = json.load(f)
    json_content = jsonify(data)
    return json_content

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3001, debug=True)
