__author__ = 'junpan'

from pymongo import MongoClient, GEO2D,ASCENDING,DESCENDING
import numpy as np
from Util import distance_kilos
import json

if __name__ == "__main__":
    #connect mongo server
    client = MongoClient('localhost', 27017)
    #connect to yelpdb
    db = client['yelpdb']
    #get business collection
    business_collection = db['business']
    cluster_collection = db['demo_cluster']

    data_raw = np.genfromtxt("prediction_RPFT.csv", delimiter=',' , dtype=float,skip_header=1)

    result_data = data_raw[:,2]


    clusters = range(0,80)
    clusters =  sorted(clusters,key=lambda x: result_data[x])


    result = []
    for cluster in clusters:
        cluster_entity = cluster_collection.find_one({"_id":cluster})
        business_in_cluster = business_collection.find({"Demo_Cluster":cluster})
        # farthest_business = max(business_in_cluster,key=lambda x: distance_kilos(cluster_entity['Centroid_Latitude'],
        #                                                              cluster_entity['Centroid_Longitude'],
        #                                                              x['loc'][1],x['loc'][0]))
        # print type(business_in_cluster)
        distance_list = map(lambda x: distance_kilos(cluster_entity['Centroid_Latitude'],
                                                                cluster_entity['Centroid_Longitude'],
                                                                x['loc'][1],x['loc'][0])
                                                               , business_in_cluster)
        dict = {}
        dict['radius'] = 1000* sum(distance_list)/len(distance_list)
        # dict['radius'] = 1000*distance_kilos(cluster_entity['Centroid_Latitude'],
        #                                                              cluster_entity['Centroid_Longitude'],
        #                                                              farthest_business['loc'][1],farthest_business['loc'][0])
        dict['darkness'] = result_data[cluster]
        dict['lat'] = cluster_entity['Centroid_Latitude']
        dict['long'] = cluster_entity['Centroid_Longitude']
        dict['id'] = cluster
        # print dict
        result.append(dict)

    with open("Phoenix_reviewpertruck_result.json", "w") as outfile:
        json.dump(result, outfile, indent=4)

