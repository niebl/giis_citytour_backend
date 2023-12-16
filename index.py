#!/usr/bin/env python

from flask import Flask, request, jsonify, Response, send_from_directory
from flask_cors import CORS
from markupsafe import escape
import json
import os

from lorem import get_paragraph

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

@app.get('/story', defaults={'story_id': False})
@app.get('/story/<story_id>')
def get_story(story_id):
    return f'story selected {story_id}'

@app.get("/desc", defaults={'desc_id': False})
@app.get("/desc/<desc_id>")
def get_desc(desc_id):
    if not desc_id:
        return('TODO: return list of all descriptions')
    if desc_id == 'template': #remove later
        return( get_paragraph(count=5, comma=(0, 2), word_range=(4, 8), sentence_range=(5, 10), sep=os.linesep) )

# media resource
# serves static files
# media_id is the filename of the file to be served
@app.get("/media", defaults={'media_id': False})
@app.get("/media/<media_id>")
def get_media(media_id):
    if not media_id:
        return Response(
            "resource not found", 
            status=404
        )    
    return send_from_directory("./media", media_id)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3001, debug=True)