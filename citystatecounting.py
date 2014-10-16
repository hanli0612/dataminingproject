#!/usr/bin/python

import json
import os
from pymongo import MongoClient, GEO2D,ASCENDING,DESCENDING
import datetime


if __name__ == "__main__":
    #connect mongo server
    client = MongoClient('localhost', 27017)
    #connect to yelpdb
    db = client['yelpdb']
    #get business collection
    business_collection = db['business']
    business_collection.ensure_index([("city", ASCENDING)])
    business_collection.ensure_index([("state", ASCENDING)])

    states = business_collection.distinct("state")
    states_list = []
    map(lambda x: states_list.append((x, business_collection.find({'state': x}).count())), states)
    for state in sorted(states_list, key=lambda x: x[1], reverse=True):
        print state[0], "has ", state[1]


    cities = business_collection.distinct("city")
    city_list = []
    map(lambda x: city_list.append((x, business_collection.find({'city': x}).count())), cities)
    for city in sorted(city_list, key=lambda x: x[1], reverse=True):
        print city[0],"has ",city[1]





