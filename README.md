dataminingproject
=================

## yelp?

* **business_checkin_dump.py:**
  The script reads business.json and checkin.json and dumps to business collection in yelpdb
  It generates the db so no need to run it. This is only for demonstration
  
* **citystatecounting.py:** 
  It counts how many businesses in each state, how many businesses in each city

* **Lasvegas_business_map.py:**
  It queries all businesses from Lasvegas, separate them to food and nofood businesses, and dumps a json file
  
* **mapdemo.html:**
  It reads json file dumped by Lasvegas_business_map.py and visualizes all businesses on google map