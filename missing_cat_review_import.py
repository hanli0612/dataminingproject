__author__ = 'junpan'


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

    review_collection = db['review']

    #make sure city and state fields are indexed
    business_collection.ensure_index([("city", ASCENDING)])
    business_collection.ensure_index([("state", ASCENDING)])
    business_collection.ensure_index([("categories", ASCENDING)])

    # review_collection.ensure_index([("text", ASCENDING)])

    unknown_business = business_collection.find({"city": {"$in": ["Phoenix", "Mesa", "Gilbert", "Tempe", "Scottsdale", "Chandler", "Glendale"]}, "categories":{"$size": 0}})
    print unknown_business.count()

    id_list = []
    for bus in unknown_business:
        id_list.append(bus['_id'])

    #
    # with open('yelp_academic_dataset_review.json') as f:
    #     for line in f:
    #         #for each line, find the corresponding business in db, add another entry called "checkin_info"
    #         one_review = json.loads(line)
    #         if one_review['business_id'] in id_list:
    #             key = one_review['review_id']
    #             one_review['_id'] = key
    #             del one_review['review_id']
    #             review_collection.insert(one_review)
    #         # print key
    #
    # print review_collection.find().count()

