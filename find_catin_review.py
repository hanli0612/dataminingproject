__author__ = 'junpan'


__author__ = 'junpan'


import json
import os
from pymongo import MongoClient, GEO2D,ASCENDING,DESCENDING
import datetime


def update_collection_push(collection, query, term):
    collection.update(query, {'$push': term})

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

    review_collection.ensure_index([('text', 'text')])


    review_match = review_collection.find( { "$text": { "$search": "drink food restaurant taste eat cafe cook breakfast diner dinner lunch fastfood pub" } } )

    print review_match.count()
    for review in review_match:
        id = review['business_id']
        business = business_collection.find_one({"_id":id})

        #print business['name']
        # print id
        if len(business['categories']) == 0:
            update_collection_push(business_collection, {'_id': id}, {'categories': 'food'})
        # print business['categories']


