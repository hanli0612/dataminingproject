__author__ = 'junpan'


import os
import numpy as np
from pymongo import MongoClient, GEO2D, ASCENDING, DESCENDING

if __name__ == "__main__":
    # connect mongo server
    client = MongoClient('localhost', 27017)
    # connect to yelpdb
    db = client['yelpdb']
    #get business collection
    cluster_collection = db['cluster']

    one = cluster_collection.find_one()
    for name in sorted(one.keys()):
        print name