import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor

data_raw = np.genfromtxt("clusters_new2.csv", delimiter=',' , dtype=float, skip_header=1)

non_zero_row = []
for i in range(len(data_raw)):
	if data_raw[i][0] != 0:
		non_zero_row.append(i)

data = data_raw[non_zero_row, :]
food_truck_num = data[:,0]
X = []
tmp = [0 for i in range(41)]
for i in range(len(data)):
	# Food Business: total checkin, Non-Food Business: total checkin, other features
	tmp[0] = data[i][8] + data[i][9] + data[i][10] + data[i][11] + data[i][12] + data[i][13]
	tmp[1] = data[i][14] + data[i][15] + data[i][16] + data[i][17] + data[i][18] + data[i][19]
	tmp[2:40] = data[np.arange(20,58)]
	print tmp

print X
