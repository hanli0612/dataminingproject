import json
import os
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

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
    	business_collection.ensure_index([("city",ASCENDING),("categories", ASCENDING)])
	
	#Total business
	total_business = business_collection.find({"city": {"$in": ["Phoenix", "Mesa", "Gilbert", "Tempe", "Scottsdale", "Chandler", "Glendale"]}})

	X = []
	Y = []
	for item in total_business:
		X.append(item['loc'])
		Y.append(item['_id'])

	#Select best K
	#K = []
	#D = []
	#for i in range(20, 200, 5):
	#	est = KMeans(n_clusters=i)
	#	est.fit(X)
	#	D.append(est.inertia_)
	#	K.append(i)

	#plt.plot(K,D)
	#plt.show()	

	K = 80
	est = KMeans(n_clusters = K)
	est.fit(X)
	labels = est.labels_
	centroids = est.cluster_centers_

	#Update DB
	# for i in range(len(labels)):
	# 	business_collection.update({'_id': Y[i]}, {'$set': {'Cluster': int(labels[i])}}, upsert = True)

	for i in range(0, K):
		cluster_collection.update({'_id': i}, {'$set': {'Centroid: Longitude': centroids[i][0], 'Centroid: Latitude': centroids[i][1]}})

	X = np.array(X)
	plt.scatter(X[:,0], X[:,1], c = labels.astype(np.float))
	plt.show()

	#h = .0002
	#x_min, x_max = X[:, 0].min(), X[:, 0].max()
	#y_min, y_max = X[:, 1].min(), X[:, 1].max()
	#xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h), sparse = True)
	#Z = est.predict(np.c_[xx.ravel(), yy.ravel()])
	#Z = Z.reshape(xx.shape)

	#plt.imshow(Z, interpolation = 'nearest', extent=(xx.min(), xx.max(), yy.min(), yy.max()), cmap=plt.cm.Paired, aspect='auto', origin='lower')
	#plt.show()
