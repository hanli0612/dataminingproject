import json
import os
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale

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

	K = 100
	est = KMeans(n_clusters = K, init='random', random_state = 10)
	est.fit(X)
	labels = est.labels_
	centroids = est.cluster_centers_

	print labels 
	
    	#Insert into DB
    	for i in range(0, K):
        	one_cluster = {}
        	one_cluster['_id'] = i + 380
        	cluster_collection.insert(one_cluster)

	#Update DB
	for i in range(len(labels)):
		business_collection.update({'_id': Y[i]}, {'$set': {'Cluster': int(labels[i])}}, upsert = True)

	for i in range(0, K):
		cluster_collection.update({'_id': i+380}, {'$set': {'Centroid: Longitude': centroids[i][0], 'Centroid: Latitude': centroids[i][1]}})

	X = np.array(X)
	#plt.scatter(X[:,0], X[:,1], c = labels.astype(np.float))
	#plt.show()
	
	# Plot the decision boundary. For that, we will assign a color to each
	x_min, x_max = X[:, 0].min(), X[:, 0].max()
	y_min, y_max = X[:, 1].min(), X[:, 1].max()
	h1 = (x_max - x_min)/2000
	h2 = (y_max - y_min)/2000
	xx, yy = np.meshgrid(np.arange(x_min, x_max, h1), np.arange(y_min, y_max, h2))
	Z = est.predict(np.c_[xx.ravel(), yy.ravel()])
	Z = Z.reshape(xx.shape)
	plt.figure(1)
	plt.clf()
	plt.imshow(Z, interpolation='nearest', extent=(xx.min(), xx.max(), yy.min(), yy.max()), cmap=plt.cm.Paired, aspect='auto', origin='lower')
	plt.plot(X[:, 0], X[:, 1], 'ko', markersize=3)	
	centroids = est.cluster_centers_
	plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', s=100, linewidths=2, color='w', zorder=10)
	plt.xlabel('Longitude')
	plt.ylabel('Latitude')
	plt.title('K-means clustering on All Business in Phoenix Area\n''Centroids are marked with white cross')
	plt.xlim(x_min, x_max)
	plt.ylim(y_min, y_max)
	plt.xticks(())
	plt.yticks(())
	plt.show()
