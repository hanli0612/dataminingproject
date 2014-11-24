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

    #make sure city and state fields are indexed
    business_collection.ensure_index([("city", ASCENDING)])
    business_collection.ensure_index([("state", ASCENDING)])
    business_collection.ensure_index([("city",ASCENDING),("categories", ASCENDING)])

    #Total business number in Las Vegas
    print "Total business", business_collection.find({"city": "Las Vegas"}).count()

    #find all businesses with the categories:"Buffets","Restaurants", "Food","Diners"
    #lasvegas_food = business_collection.find({"city": "Las Vegas","categories": {"$in": ["Buffets","Restaurants", "Food","Diners"]}})
    lasvegas_food = business_collection.find({"city": {"$in":["Phoenix","Glendale","Scottsdale","Tempe","Mesa","Gilbert","Chandler"]},"categories": {"$in": ["Food Trucks","Street Vendors", "Food Stands", "Caterers","Delis"]}})
    # lasvegas_food = business_collection.find({"city": {"$in":["Phoenix","Glendale","Scottsdale","Tempe","Mesa","Gilbert","Chandler"]},"categories": {"$in": ["Buffets","Restaurants", "Food","Diners"]}})
    business_food_list = []
    for business in lasvegas_food:
        # appending name, lng,lat to list
        business_food_list.append({"name": business['name'], "lng": business["loc"][0], "lat":business["loc"][1]})

    #Total number of food business
    print "food", len(business_food_list)

    #find all businesses without the categories:"Buffets","Restaurants", "Food","Diners"
    lasvegas_nofood = business_collection.find({"city": {"$in":["Phoenix","Glendale","Scottsdale","Tempe","Mesa","Gilbert","Chandler"]},"categories": {"$nin": ["Buffets","Restaurants", "Food","Diners"]}})
    business_nofood_list = []
    for business in lasvegas_nofood:
        business_nofood_list.append({"name": business['name'], "lng": business["loc"][0], "lat":business["loc"][1]})

    #Total number of food business
    print "nofood", len(business_nofood_list)

    #put 2 lists to dictionary
    business_dict = {"business_food": business_food_list,"business_nofood": business_nofood_list}

    #dump json file
    with open("lasvagas.json", "w") as outfile:
        json.dump(business_dict, outfile, indent=4)

