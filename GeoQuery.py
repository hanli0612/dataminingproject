__author__ = 'junpan'

from pymongo import MongoClient, GEO2D, ASCENDING, DESCENDING

if __name__ == "__main__":
    #connect mongo server
    client = MongoClient('localhost', 27017)
    #connect to yelpdb
    db = client['yelpdb']
    #get business collection
    business_collection = db['business']
    cluster_collection = db['cluster']

        #make sure city and state fields are indexed
    business_collection.ensure_index([("city", ASCENDING)])
    business_collection.ensure_index([("state", ASCENDING)])
    # business_collection.ensure_index([("ClusterBearBy", ASCENDING)])
    business_collection.ensure_index([("city",ASCENDING),("categories", ASCENDING)])
    business_collection.ensure_index([("loc", GEO2D)])

    #Total business
    food_Trucks = business_collection.find({"city": {"$in":["Phoenix","Glendale","Scottsdale","Tempe","Mesa","Gilbert","Chandler"]},"categories": {"$in": ["Food Trucks","Street Vendors", "Food Stands", "Caterers","Delis"]}})

    print food_Trucks.count()

    # business_collection.update({"ClusterBearBy": { "$exists": True }}, {"$unset": {"ClusterBearBy":""}})
    count = 0
    for food_Truck in food_Trucks:
        loc = food_Truck['loc'];
        nearby_business = business_collection.find({"loc": {"$within": {"$center": [loc, 0.015]}}})
        # print nearby_business.count()
        for business in nearby_business:
            business_collection.update({'_id': business['_id']}, {'$push': {"ClusterNearBy":count}})
        count +=1

