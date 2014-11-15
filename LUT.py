import os
import numpy as np
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

        K = 80	
	food_review = [0 for i in range(0,K)] 
	nofood_review = [0 for i in range(0,K)]
	truck_num = [0 for i in range(0,K)]
	truck_review = [0 for i in range(0,K)]
	truck_checkin = [0 for i in range(0,K)]
	food_1star = [0 for i in range(0,K)]
	food_2star = [0 for i in range(0,K)] 
	food_3star = [0 for i in range(0,K)]
	food_4star = [0 for i in range(0,K)] 
	food_5star = [0 for i in range(0,K)]
        nofood_1star = [0 for i in range(0,K)]
        nofood_2star = [0 for i in range(0,K)]
        nofood_3star = [0 for i in range(0,K)]
        nofood_4star = [0 for i in range(0,K)]
        nofood_5star = [0 for i in range(0,K)]
	food_0am_checkin = [0 for i in range(0,K)]
	food_4am_checkin = [0 for i in range(0,K)]
	food_8am_checkin = [0 for i in range(0,K)]
	food_12pm_checkin = [0 for i in range(0,K)]
	food_4pm_checkin = [0 for i in range(0,K)]
	food_8pm_checkin = [0 for i in range(0,K)]
        nofood_0am_checkin = [0 for i in range(0,K)]
        nofood_4am_checkin = [0 for i in range(0,K)]
        nofood_8am_checkin = [0 for i in range(0,K)]
        nofood_12pm_checkin = [0 for i in range(0,K)]
        nofood_4pm_checkin = [0 for i in range(0,K)]
        nofood_8pm_checkin = [0 for i in range(0,K)]
        truck_0am_checkin = [0 for i in range(0,K)]
        truck_4am_checkin = [0 for i in range(0,K)]
        truck_8am_checkin = [0 for i in range(0,K)]
        truck_12pm_checkin = [0 for i in range(0,K)]
        truck_4pm_checkin = [0 for i in range(0,K)]
        truck_8pm_checkin = [0 for i in range(0,K)]
	
	food_1price = [0 for i in range(0,K)] 
	food_2price = [0 for i in range(0,K)]
	food_3price = [0 for i in range(0,K)]
	food_4price = [0 for i in range(0,K)]
        nofood_1price = [0 for i in range(0,K)]
        nofood_2price = [0 for i in range(0,K)]
        nofood_3price = [0 for i in range(0,K)]
        nofood_4price = [0 for i in range(0,K)]
	num_accept_credit_card = [0 for i in range(0,K)]
	num_caters = [0 for i in range(0,K)]
	num_delivery = [0 for i in range(0,K)]
	num_drive_through = [0 for i in range(0,K)]
	average_noise_level = [0 for i in range(0,K)]
	loud_noise_level = [0 for i in range(0,K)]
	quiet_noise_level = [0 for i in range(0,K)]
	num_takeout = [0 for i in range(0,K)]
	num_good_for_group = [0 for i in range(0,K)]
	num_good_for_kid = [0 for i in range(0,K)]
	num_outdoor_seating = [0 for i in range(0,K)]
	num_breakfast = [0 for i in range(0,K)]
	num_brunch = [0 for i in range(0,K)]
	num_dessert = [0 for i in range(0,K)]
	num_dinner = [0 for i in range(0,K)]
	num_latenight = [0 for i in range(0,K)]
	num_lunch = [0 for i in range(0,K)]
	num_take_reservation = [0 for i in range(0,K)]
	num_waiter_service = [0 for i in range(0,K)]
	num_wifi = [0 for i in range(0,K)]
	num_garage_parking = [0 for i in range(0,K)]
	num_lot_parking = [0 for i in range(0,K)]
	num_street_parking = [0 for i in range(0,K)]
	num_valet_parking = [0 for i in range(0,K)]
	num_validated_parking = [0 for i in range(0,K)]


	for item in total_business:
		if "Food Trucks" in item['categories'] or 'Street Vendors' in item['categories'] or 'Food Stands' in item['categories'] or 'Caterers' in item['categories']:
			if item['open']:
				truck_num[item['Cluster']] += 1
				truck_review[item['Cluster']] += item['review_count']
                                #Checkin Info
                                if "checkin_info" in item.keys():
                                        for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
                                                for hour in range(0, 23):
                                                	if day in item['checkin_info'].keys():
                                                        	if str(hour) in item['checkin_info'][day].keys():
                                                                	if 0<=hour or 4>hour:
                                                                                truck_0am_checkin[item['Cluster']] += item['checkin_info'][day][str(hour)]
                                                                        if 4<=hour or 8>hour:
                                                                                truck_4am_checkin[item['Cluster']] += item['checkin_info'][day][str(hour)]
                                                                        if 8<=hour or 12>hour:
                                                                                truck_8am_checkin[item['Cluster']] += item['checkin_info'][day][str(hour)]
                                                                        if 12<=hour or 16>hour:
                                                                               	truck_12pm_checkin[item['Cluster']] += item['checkin_info'][day][str(hour)]
                                                                        if 16<=hour or 20>hour:
                                                                                truck_4pm_checkin[item['Cluster']] += item['checkin_info'][day][str(hour)]
                                                                        if 20<=hour or 24>hour:
                                                                                truck_8pm_checkin[item['Cluster']] += item['checkin_info'][day][str(hour)]
	 	#Food Business	
		elif "Buffets" in item['categories'] or "Restaurants" in item['categories'] or "Diners" in item['categories'] or "Cafe" in item['categories']:
			if item['open']:
				food_review[item['Cluster']] += item['review_count']
				#Rating Info
				if (0.0 < item['stars']) and (1.0 >= item['stars']):
					food_1star[item['Cluster']] += 1
				elif (1.0 < item['stars']) and (2.0 >= item['stars']):
					food_2star[item['Cluster']] += 1
                                elif (2.0 < item['stars']) and (3.0 >= item['stars']):
                                        food_3star[item['Cluster']] += 1
                                elif (3.0 < item['stars']) and (4.0 >= item['stars']):
                                        food_4star[item['Cluster']] += 1
				else:
					food_5star[item['Cluster']] += 1

				#Price Info
				if "Price Range" in item['attributes'].keys():
                                	if 0 < item['attributes']['Price Range'] and 1 >= item['attributes']['Price Range']:
                                        	food_1price[item['Cluster']] += 1
					elif 1 < item['attributes']['Price Range'] and 2 >= item['attributes']['Price Range']:
                                        	food_2price[item['Cluster']] += 1
                                	elif 2 < item['attributes']['Price Range'] and 3 >= item['attributes']['Price Range']:
                                        	food_3price[item['Cluster']] += 1
					else:
						food_4price[item['Cluster']] += 1
				
				#Credit Card
				if "Accepts Credit Cards" in item['attributes'].keys():
					if item['attributes']['Accepts Credit Cards']:
						num_accept_credit_card[item['Cluster']] += 1

				#Caters
				if "Caters" in item['attributes'].keys():
					if item['attributes']['Caters']:
						num_caters[item['Cluster']] += 1

				#Delivery
				if "Delivery" in item['attributes'].keys():
					if item['attributes']['Delivery']:
						num_delivery[item['Cluster']] += 1
				
				#Drive through
				if "Drive-Thru" in item['attributes'].keys():
					if item['attributes']['Drive-Thru']:
						num_drive_through[item['Cluster']] += 1

				#Noise 
				if "Noise Level" in item['attributes'].keys():
					if item['attributes']['Noise Level'] == 'average':
						average_noise_level[item['Cluster']] += 1
					elif item['attributes']['Noise Level'] == 'loud':
						loud_noise_level[item['Cluster']] += 1
					elif item['attributes']['Noise Level'] == 'quiet':
						quiet_noise_level[item['Cluster']] += 1

				#Takeout
				if "Take-out" in item['attributes'].keys():
					if item['attributes']['Take-out']:
						num_takeout[item['Cluster']] += 1

				#Reservation
				if "Take Reservations" in item['attributes'].keys():
					if item['attributes']['Take Reservations']:
       	 					num_take_reservation[item['Cluster']] += 1

				#Waiter
				if "Waiter Service" in item['attributes'].keys():
					if item['attributes']['Waiter Service']:
        					num_waiter_service[item['Cluster']] += 1

				#Wi-Fi
				if "Wi-Fi" in item['attributes'].keys():
					if item['attributes']['Wi-Fi']:
        					num_wifi[item['Cluster']] += 1

                                #Groups
                                if "Good For Groups" in item['attributes'].keys():
                                        if item['attributes']['Good For Groups']:
        					num_good_for_group[item['Cluster']] += 1

                                #Kids
                                if "Good For Kids" in item['attributes'].keys():
                                        if item['attributes']['Good For Kids']:
						num_good_for_kid[item['Cluster']] += 1

				#Outdoor Seating
				if "Outdoor Seating" in item['attributes'].keys():
					if item['attributes']['Outdoor Seating']:
        					num_outdoor_seating[item['Cluster']] += 1

				#Good For
				if "Good For" in item['attributes'].keys():
					if "breakfast" in item['attributes']['Good For']:
						if item['attributes']['Good For']['breakfast']:
        						num_breakfast[item['Cluster']] += 1
                                        if "brunch" in item['attributes']['Good For']:                                        
						if item['attributes']['Good For']['brunch']:
        						num_brunch[item['Cluster']] += 1
                                        if "dessert" in item['attributes']['Good For']:                                        
						if item['attributes']['Good For']['dessert']:
        						num_dessert[item['Cluster']] += 1
                                        if "dinner" in item['attributes']['Good For']:                                        
						if item['attributes']['Good For']['dinner']:
        						num_dinner[item['Cluster']] += 1
                                        if "latenight" in item['attributes']['Good For']:                                        
						if item['attributes']['Good For']['latenight']:
        						num_latenight[item['Cluster']] += 1
                                        if "lunch" in item['attributes']['Good For']:                                        
						if item['attributes']['Good For']['lunch']:
        						num_lunch[item['Cluster']] += 1
				
				#Parking
				if "Parking" in item['attributes'].keys():
					if "garage" in item['attributes']['Parking']:
						if item['attributes']['Parking']['garage']:
        						num_garage_parking[item['Cluster']] += 1
                                        if "lot" in item['attributes']['Parking']:                                
						if item['attributes']['Parking']['lot']:
      							num_lot_parking[item['Cluster']] += 1
                                        if "street" in item['attributes']['Parking']:
                                        	if item['attributes']['Parking']['street']:
        						num_street_parking[item['Cluster']] += 1
                                        if "valet" in item['attributes']['Parking']:
                                        	if item['attributes']['Parking']['valet']:
        						num_valet_parking[item['Cluster']] += 1
                                        if "validated" in item['attributes']['Parking']:
                                        	if item['attributes']['Parking']['validated']:
        						num_validated_parking[item['Cluster']] += 1

				#Checkin Info
				if "checkin_info" in item.keys():
                                        for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
                                                for hour in range(0, 23):
                                                        if day in item['checkin_info'].keys():
                                                        	if str(hour) in item['checkin_info'][day].keys():
									if 0<=hour or 4>hour:
										food_0am_checkin[item['Cluster']] += item['checkin_info'][day][str(hour)]
									if 4<=hour or 8>hour:
										food_4am_checkin[item['Cluster']] += item['checkin_info'][day][str(hour)]
                                                                        if 8<=hour or 12>hour:
                                                                                food_8am_checkin[item['Cluster']] += item['checkin_info'][day][str(hour)]
                                                                        if 12<=hour or 16>hour:
                                                                                food_12pm_checkin[item['Cluster']] += item['checkin_info'][day][str(hour)]
                                                                        if 16<=hour or 20>hour:
                                                                                food_4pm_checkin[item['Cluster']] += item['checkin_info'][day][str(hour)]
                                                                        if 20<=hour or 24>hour:
                                                                                food_8pm_checkin[item['Cluster']] += item['checkin_info'][day][str(hour)]
										
									
		else:						
                        if item['open']:
                                nofood_review[item['Cluster']] += item['review_count']
                                if 0 < item['stars'] and 1 >= item['stars']:
                                        nofood_1star[item['Cluster']] += 1
                                elif 1 < item['stars'] and 2 >= item['stars']:
                                        nofood_2star[item['Cluster']] += 1
                                elif 2 < item['stars'] and 3 >= item['stars']:
                                        nofood_3star[item['Cluster']] += 1
                                elif 3 < item['stars'] and 4 >= item['stars']:
                                        nofood_4star[item['Cluster']] += 1
                                else:
                                        nofood_5star[item['Cluster']] += 1

                                if "Price Range" in item['attributes'].keys():
                                        if 0 < item['attributes']['Price Range'] and 1 >= item['attributes']['Price Range']:
                                                nofood_1price[item['Cluster']] += 1
                                        elif 1 < item['attributes']['Price Range'] and 2 >= item['attributes']['Price Range']:
                                                nofood_2price[item['Cluster']] += 1
                                        elif 2 < item['attributes']['Price Range'] and 3 >= item['attributes']['Price Range']:
                                                nofood_3price[item['Cluster']] += 1
                                        else:
                                                nofood_4price[item['Cluster']] += 1

                                #Checkin Info
                                if "checkin_info" in item.keys():
                                        for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
                                                for hour in range(0, 23):
                                                	if day in item['checkin_info'].keys():
                                                        	if str(hour) in item['checkin_info'][day].keys():
                                                                	if 0<=hour or 4>hour:
                                                                                nofood_0am_checkin[item['Cluster']] += item['checkin_info'][day][str(hour)]
                                                                        if 4<=hour or 8>hour:
                                                                                nofood_4am_checkin[item['Cluster']] += item['checkin_info'][day][str(hour)]
                                                                        if 8<=hour or 12>hour:
                                                                                nofood_8am_checkin[item['Cluster']] += item['checkin_info'][day][str(hour)]
                                                                        if 12<=hour or 16>hour:
                                                                               	nofood_12pm_checkin[item['Cluster']] += item['checkin_info'][day][str(hour)]
                                                                        if 16<=hour or 20>hour:
                                                                                nofood_4pm_checkin[item['Cluster']] += item['checkin_info'][day][str(hour)]
                                                                        if 20<=hour or 24>hour:
                                                                                nofood_8pm_checkin[item['Cluster']] += item['checkin_info'][day][str(hour)]
	
	#Remove DB
	#for i in range(0, 80):
	#	cluster_collection.remove()

	#Insert into DB
	#for i in range(0, K):
	#	one_cluster = {}
	#	one_cluster['_id'] = i
	#	cluster_collection.insert(one_cluster)

	#Write Values
	for i in range(0, K):
		cluster_collection.update({"_id": i}, {"$set": {"Food Truck Num": truck_num[i], "Food Review": food_review[i], "No Food Review": nofood_review[i], "Food Truck Review": truck_review[i], "Food Truck Checkin": truck_checkin[i], "Food: 1 Star": food_1star[i], "Food: 2 Star": food_2star[i], "Food: 3 Star": food_3star[i], "Food: 4 Star": food_4star[i], "Food: 5 Star": food_5star[i], "No Food: 1 Star": nofood_1star[i], "No Food: 2 Star": nofood_2star[i], "No Food: 3 Star": nofood_3star[i], "No Food: 4 Star": nofood_4star[i], "No Food: 5 Star": nofood_5star[i]}})
		cluster_collection.update({"_id":i}, {"$set": {"0am Food Checkin": food_0am_checkin[i], "4am Food Checkin": food_4am_checkin[i], "8am Food Checkin": food_8am_checkin[i], "12pm Food Checkin": food_12pm_checkin[i], "4pm Food Checkin": food_4pm_checkin[i], "8pm Food Checkin": food_8pm_checkin[i]}})
		cluster_collection.update({"_id":i}, {"$set": {"0am No Food Checkin": nofood_0am_checkin[i], "4am No Food Checkin": nofood_4am_checkin[i], "8am No Food Checkin": nofood_8am_checkin[i], "12pm No Food Checkin": nofood_12pm_checkin[i], "4pm No Food Checkin": nofood_4pm_checkin[i], "8pm No Food Checkin": nofood_8pm_checkin[i]}})
		cluster_collection.update({"_id":i}, {"$set": {"0am Food Truck Checkin": truck_0am_checkin[i], "4am Food Truck Checkin": truck_4am_checkin[i], "8am Food Truck Checkin": truck_8am_checkin[i], "12pm Food Truck Checkin": truck_12pm_checkin[i], "4pm Food Truck Checkin": truck_4pm_checkin[i], "8pm Food Truck Checkin": truck_8pm_checkin[i]}})
		cluster_collection.update({"_id": i}, {"$set": {"Food: 1 Price": food_1price[i], "Food: 2 Price": food_2price[i], "Food: 3 Price": food_3price[i], "Food: 4 Price ": food_4price[i], "No Food: 1 Price": nofood_1price[i], "No Food: 2 Price": nofood_2price[i], "No Food: 3 Price": nofood_3price[i], "No Food: 4 Price": nofood_4price[i]}})
		cluster_collection.update({"_id": i}, {"$set": {"Credit Card": num_accept_credit_card[i], "Cater": num_caters[i], "Delivery": num_delivery[i], "Drive-thru": num_drive_through[i], "Noise: Quiet": quiet_noise_level[i], "Noise: Average": average_noise_level[i], "Noise: Loud": loud_noise_level[i], "Takeout": num_takeout[i], "Good for Groups": num_good_for_group[i], "Good for Kids": num_good_for_kid[i], "Outdoor Seating": num_outdoor_seating[i], "Reservation": num_take_reservation[i], "Waiter Service": num_waiter_service[i], "Wi-Fi": num_wifi[i], "Parking: Garage": num_garage_parking[i], "Parking: Lot": num_lot_parking[i], "Parking: Street": num_street_parking[i], "Parking: Valet": num_valet_parking[i], "Parking: Validated": num_validated_parking[i]}})




