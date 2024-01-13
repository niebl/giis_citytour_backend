#!/usr/bin/env python

import json
import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify, Response, send_from_directory
from flask_cors import CORS, cross_origin
#from markupsafe import escape
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL

from lorem import get_paragraph

from classes import Story, Site 

load_dotenv()

url = URL.create(
    drivername="postgresql",
    username=os.getenv("DB_USER"),
    host=os.getenv("DB_URL"),
    database="giis",
    password=os.getenv("DB_PASSWORD")
)
db_engine = create_engine(url)

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
def index():
    return (
'''
/template-data: &nbsp               placeholder, serves GeoJSON formatted example story <br/>
/story/&lt;story_id&gt;: &nbsp      serves the GeoJSON formatted tour-route data of the given story-id <br/>
/media/&lt;filename&gt;: &nbsp      serves a file that corresponds to the filname, if a corresponding file exists in the media directory
'''
    )
    
@app.get("/template-data")
def get_poi():
    f = open("./templateData/points.json")
    data = json.load(f)
    json_content = jsonify(data)
    return json_content

@app.get('/story', defaults={'story_id': False})
@app.get('/story/<story_id>')
def get_story(story_id):
    story = Story(story_id)
    return str(story)

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