#!/usr/bin/python

import json
import os
from pymongo import MongoClient, GEO2D
import datetime


#print some queries from collection for testing.....
def example_print(collection, n):
    for doc in collection.find().limit(n):
        print doc

#update/add one or more fields of a single entry(business)
def update_collection(collection, query, term):
    collection.update(query, {'$set': term})

#find all enties(business) with the field exist
def find_exist(collection, field_name):
    return collection.find({field_name: {"$exists": True}})

if __name__ == "__main__":
    #connect mongo server
    client = MongoClient('localhost', 27017)
    #connect to yelpdb
    db = client['yelpdb']
    #get business collection
    business_collection = db['business']


    #create geo index for geo location query
    business_collection.create_index([("loc", GEO2D)])


    # open business.json
    with open('yelp_academic_dataset_business.json') as f:
        for line in f:
            #load each business as dictionary
            one_business = json.loads(line)

            #use business_id as the key to the db entry ("_id")
            key = one_business['business_id']
            one_business['_id'] = key
            del one_business['business_id']

            #change lng,lat to the format mongodb wants
            lng = float(one_business['longitude'])
            lat = float(one_business['latitude'])
            one_business['loc'] = [lng,lat]
            del one_business['longitude']
            del one_business['latitude']

            #insert this business to business collection
            business_collection.insert(one_business)

    #open checkin.json
    with open('yelp_academic_dataset_checkin.json') as f:
        for line in f:
            #for each line, find the corresponding business in db, add another entry called "checkin_info"
            one_checkin = json.loads(line)
            business_key = one_checkin['business_id']
            update_collection(business_collection, {'_id': business_key}, {'checkin_info': one_checkin['checkin_info']})



