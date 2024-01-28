#!/usr/bin/env python

import json
import os
import copy
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL

class Story:
    story_id: int
    story_tite: str
    story_description: str

    sites: list

    def __init__(self, story_id):
        load_dotenv()
        url = URL.create(
            drivername="postgresql",
            username=os.getenv("DB_USER"),
            host=os.getenv("DB_URL"),
            port=os.getenv("DB_PORT"),
            database="giis",
            password=os.getenv("DB_PASSWORD")
        )
        db_engine = create_engine(url)

        #all stories
        if story_id == "all":
            #sites
            self.sites = []
            with db_engine.connect() as connection:
                db_sites = connection.execute(text(f"SELECT * FROM sites"))
                sites = [row._asdict() for row in db_sites]
                for site in sites:
                    self.sites.append(Site(site))
                return

        #select story_id
        story = False
        with db_engine.connect() as connection:
            db_story = connection.execute(text(f"SELECT * FROM stories WHERE story_id={story_id}"))    
        results = [row._asdict() for row in db_story]
        if len(results) != 1:
            raise ValueError
        res = results[0]

        self.story_id = res["story_id"]
        self.story_title = res["story_title"]
        self.story_description = res["story_description"]

        #sites
        self.sites = []
        with db_engine.connect() as connection:
            db_sites = connection.execute(text(f"SELECT * FROM sites WHERE story={story_id}"))
            sites = [row._asdict() for row in db_sites]
            for site in sites:
                self.sites.append(Site(site))

    def __str__(self):
        out = copy.copy(self)
        out.features = []
        return json.dumps(self.toGeoJSON())


    def toGeoJSON(self):
        out = {}
        out["type"] = "FeatureCollection"
        out["features"] = []
        for site in self.sites:
            out["features"].append(site.toGeoJSON())
        return out


class Site:
    site_id: int
    story: int

    coordinates: tuple
    site_index: int
    site_name: str

    short_desc: str
    long_desc: str
    short_story: str
    long_story: str
    image_url: str
    radius: int

    def __init__(self, attribs):
        self.tour_id = attribs["story"]
        self.site_id = attribs["site_id"]
        self.coordinates = list(self.toTuple(attribs["coordinates"]))
        self.site_index = attribs["site_index"]
        
        self.site_name = attribs["site_name"]
        self.short_desc = attribs["short_desc"]
        self.long_desc = attribs["long_desc"]
        self.short_story = attribs["short_story"]
        self.long_story = attribs["long_story"]
        self.image_url = attribs["image_url"]
        self.radius = attribs["radius"]

    def __str__(self):
        return json.dumps(self.toGeoJSON())

    def toGeoJSON(self):
        out = {}
        out["type"] = "Feature"

        out["geometry"] = {}
        out["geometry"]["type"] = "Point"
        out["geometry"]["coordinates"] = list(self.coordinates)

        out["properties"] = {}
        out["properties"]["tour_id"] = self.tour_id
        out["properties"]["poi_id"] = self.site_id
        out["properties"]["name"] = self.site_name
        out["properties"]["short_desc"] = self.short_desc
        out["properties"]["long_desc"] = self.long_desc
        out["properties"]["short_story"] = self.short_story
        out["properties"]["long_story"] = self.long_story
        out["properties"]["image_url"] = self.image_url
        out["properties"]["radius"] = self.radius

        out["properties"]["site_index"] = self.site_index
        return out

    def toTuple(self, string: str):
        string = string.replace("(","")
        string = string.replace(")","")
        
        pair = string.split(",")
        pair[0] = float(pair[0])
        pair[1] = float(pair[1])
        return tuple(pair)


if __name__ == '__main__':
    print("beep")