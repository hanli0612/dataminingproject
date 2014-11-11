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
	    
	    # Format checkin_info
	    for key in one_checkin['checkin_info']:
		k = key.partition("-")
	   	time = int(k[0])
		day =  int(k[2])

		if day == 0:
			if time == 0:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Sunday.0": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 1:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Sunday.1": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 2:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Sunday.2": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 3:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Sunday.3": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 4:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Sunday.4": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 5:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Sunday.5": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 6:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Sunday.6": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 7:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Sunday.7": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 8:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Sunday.8": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 9:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Sunday.9": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 10:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Sunday.10": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 11:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Sunday.11": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 12:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Sunday.12": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 13:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Sunday.13": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 14:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Sunday.14": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 15:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Sunday.15": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 16:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Sunday.16": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 17:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Sunday.17": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 18:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Sunday.18": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 19:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Sunday.19": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 20:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Sunday.20": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 21:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Sunday.21": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 22:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Sunday.22": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			else:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Sunday.23": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
		elif day == 1:
			if time == 0:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Monday.0": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 1:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Monday.1": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 2:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Monday.2": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 3:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Monday.3": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 4:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Monday.4": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 5:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Monday.5": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 6:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Monday.6": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 7:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Monday.7": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 8:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Monday.8": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 9:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Monday.9": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 10:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Monday.10": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 11:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Monday.11": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 12:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Monday.12": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 13:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Monday.13": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 14:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Monday.14": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 15:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Monday.15": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 16:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Monday.16": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 17:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Monday.17": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 18:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Monday.18": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 19:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Monday.19": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 20:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Monday.20": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 21:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Monday.21": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 22:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Monday.22": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			else:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Monday.23": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
		elif day == 2:
			if time == 0:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Tuesday.0": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 1:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Tuesday.1": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 2:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Tuesday.2": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 3:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Tuesday.3": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 4:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Tuesday.4": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 5:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Tuesday.5": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 6:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Tuesday.6": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 7:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Tuesday.7": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 8:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Tuesday.8": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 9:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Tuesday.9": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 10:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Tuesday.10": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 11:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Tuesday.11": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 12:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Tuesday.12": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 13:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Tuesday.13": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 14:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Tuesday.14": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 15:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Tuesday.15": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 16:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Tuesday.16": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 17:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Tuesday.17": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 18:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Tuesday.18": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 19:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Tuesday.19": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 20:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Tuesday.20": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 21:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Tuesday.21": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 22:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Tuesday.22": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			else:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Tuesday.23": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
		elif day == 3:
			if time == 0:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Wednesday.0": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 1:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Wednesday.1": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 2:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Wednesday.2": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 3:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Wednesday.3": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 4:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Wednesday.4": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 5:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Wednesday.5": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 6:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Wednesday.6": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 7:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Wednesday.7": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 8:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Wednesday.8": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 9:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Wednesday.9": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 10:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Wednesday.10": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 11:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Wednesday.11": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 12:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Wednesday.12": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 13:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Wednesday.13": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 14:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Wednesday.14": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 15:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Wednesday.15": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 16:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Wednesday.16": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 17:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Wednesday.17": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 18:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Wednesday.18": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 19:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Wednesday.19": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 20:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Wednesday.20": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 21:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Wednesday.21": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 22:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Wednesday.22": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			else:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Wednesday.23": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
		elif day == 4:
			if time == 0:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Thursday.0": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 1:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Thursday.1": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 2:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Thursday.2": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 3:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Thursday.3": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 4:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Thursday.4": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 5:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Thursday.5": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 6:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Thursday.6": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 7:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Thursday.7": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 8:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Thursday.8": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 9:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Thursday.9": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 10:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Thursday.10": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 11:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Thursday.11": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 12:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Thursday.12": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 13:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Thursday.13": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 14:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Thursday.14": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 15:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Thursday.15": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 16:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Thursday.16": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 17:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Thursday.17": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 18:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Thursday.18": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 19:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Thursday.19": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 20:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Thursday.20": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 21:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Thursday.21": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 22:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Thursday.22": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			else:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Thursday.23": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
		elif day == 5:
			if time == 0:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Friday.0": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 1:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Friday.1": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 2:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Friday.2": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 3:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Friday.3": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 4:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Friday.4": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 5:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Friday.5": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 6:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Friday.6": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 7:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Friday.7": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 8:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Friday.8": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 9:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Friday.9": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 10:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Friday.10": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 11:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Friday.11": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 12:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Friday.12": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 13:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Friday.13": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 14:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Friday.14": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 15:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Friday.15": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 16:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Friday.16": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 17:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Friday.17": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 18:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Friday.18": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 19:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Friday.19": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 20:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Friday.20": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 21:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Friday.21": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 22:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Friday.22": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			else:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Friday.23": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
		else:
			if time == 0:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Saturday.0": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 1:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Saturday.1": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 2:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Saturday.2": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 3:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Saturday.3": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 4:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Saturday.4": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 5:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Saturday.5": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 6:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Saturday.6": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 7:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Saturday.7": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 8:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Saturday.8": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 9:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Saturday.9": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 10:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Saturday.10": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 11:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Saturday.11": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 12:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Saturday.12": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 13:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Saturday.13": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 14:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Saturday.14": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 15:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Saturday.15": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 16:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Saturday.16": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 17:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Saturday.17": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 18:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Saturday.18": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 19:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Saturday.19": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 20:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Saturday.20": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 21:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Saturday.21": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			elif time == 22:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Saturday.22": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
			else:
				business_collection.update({'_id': business_key},{"$set": {"checkin_info.Saturday.23": one_checkin['checkin_info'][key]}}, multi = True, upsert = True)
