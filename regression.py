__author__ = 'junpan'
from pymongo import MongoClient, GEO2D,ASCENDING,DESCENDING
import numpy as np
from sklearn.preprocessing import scale
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LassoCV
from sklearn.linear_model import Lasso
from numpy.random import randint
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import AdaBoostRegressor
import math

TIME = 5

if __name__ == "__main__":
    #connect mongo server
    client = MongoClient('localhost', 27017)
    #connect to yelpdb
    db = client['yelpdb']
    #get business collection
    business_collection = db['cluster']

    period = {}
    for i in range(0,6):
        ori = range(2,20)
        need = range(i+2,20,6)
        left = list(set(ori)-set(need))

        period[i] = left

    print period
    data_raw = np.genfromtxt("clusters_final_average.csv", delimiter=',' , dtype=float,skip_header=1)
    print data_raw.shape
    food_truck_num = data_raw[:,0]
    # print food_truck_num
    # food_truck_checkin_0am = data_raw[:,6]
    data_0am = np.delete(data_raw,period[TIME], 1)
    print data_0am.shape
    data_0am_train = data_0am[food_truck_num!=0,:]
    print "after delete foodtruck 0num" ,data_0am_train.shape
    data_0am_train = np.delete(data_0am_train,[0,1],1)
    data_0am_train_x = np.delete(data_0am_train,0,1)
    data_0am_train_y = data_0am_train[:,0]
    data_0am_train_x = scale(data_0am_train_x)

    print data_0am_train_x.shape
    print data_0am_train_y.shape


    # lr = LinearRegression()
    # lr.fit(data_0am_train_x,data_0am_train_y)
    # score = lr.score(data_0am_train_x,data_0am_train_y)
    # print score
    # # print lr.coef_
    # coef = abs(lr.coef_)
    # coef_s = [1 if i > 0 else 0 for i in coef]
    # de_array = [i for i, j in enumerate(coef_s) if j == 0]
    # print coef_s
    # # print len(de_array)
    # data_0am_train_x = np.delete(data_0am_train_x,de_array,1)
    # print data_0am_train_x.shape

    B=np.random.randint(data_0am_train_x.shape[0],size=math.ceil(data_0am_train_x.shape[0]/5))
    data_0am_test_x = data_0am_train_x[B,:]
    data_0am_test_y = data_0am_train_y[B]
    test_y_std = np.std(data_0am_test_y)
    test_y_mean = np.mean(data_0am_test_y)

    data_0am_train_xx = np.delete(data_0am_train_x,B,0)
    data_0am_train_yy = np.delete(data_0am_train_y,B)
    train_y_std = np.std(data_0am_train_yy)
    train_y_mean = np.mean(data_0am_train_yy)
    print "train data shape",data_0am_train_xx.shape
    print "test data shape", data_0am_test_x.shape

    print "train y std ", train_y_std
    print "train y mean ", train_y_mean
    print "test y std", test_y_std
    print "test y mean", test_y_mean

    # nom = (np.amax(data_0am_train_yy)-np.amin(data_0am_train_yy))
    nom_train = np.amax(data_0am_train_yy)-np.amin(data_0am_train_yy)
    nom_test = np.amax(data_0am_test_y)-np.amin(data_0am_test_y)
    lr = LinearRegression()
    lr.fit(data_0am_train_xx,data_0am_train_yy)
    data_0am_train_predy = lr.predict(data_0am_train_xx)
    linear_train_predy = lr.predict(data_0am_train_xx)

    data_0am_test_predy = lr.predict(data_0am_test_x)
    linear_test_predy = lr.predict(data_0am_test_x)
    print "Linar Regression report"
    print "train score: ", lr.score(data_0am_train_xx,data_0am_train_yy)
    print "train error: " , np.sqrt(np.mean((data_0am_train_predy-data_0am_train_yy)**2))/nom_train
    print "test error: ",  np.sqrt(np.mean((data_0am_test_predy-data_0am_test_y)**2))/nom_test

    # print "train error ratio: " , np.mean(np.divide(np.absolute(data_0am_train_predy-data_0am_train_yy),data_0am_train_yy+0.001))
    # print "train error ratio: " , np.absolute(data_0am_train_predy-data_0am_train_yy)
    # print "test error ratio: ", np.mean(np.divide(np.absolute(data_0am_test_predy-data_0am_test_y),data_0am_train_yy+0.00001))

    las = Lasso(max_iter=50000,alpha=0.01)
    las.fit(data_0am_train_xx,data_0am_train_yy)
    data_0am_train_predy = las.predict(data_0am_train_xx)
    lasso_train_predy = las.predict(data_0am_train_xx)

    data_0am_test_predy = las.predict(data_0am_test_x)
    lasso_test_predy = las.predict(data_0am_test_x)
    print "Lasso report"
    print "train score: ", las.score(data_0am_train_xx,data_0am_train_yy)
    print "train error: " , np.sqrt(np.mean((data_0am_train_predy-data_0am_train_yy)**2))/nom_train
    print "test error: ",  np.sqrt(np.mean((data_0am_test_predy-data_0am_test_y)**2))/nom_test

    svr = SVR(kernel='linear')
    svr.fit(data_0am_train_xx,data_0am_train_yy)
    data_0am_train_predy = svr.predict(data_0am_train_xx)
    svr_train_predy = svr.predict(data_0am_train_xx)

    data_0am_test_predy = svr.predict(data_0am_test_x)
    svr_test_predy = svr.predict(data_0am_test_x)
    print "SVR report"
    print "train score: ", svr.score(data_0am_train_xx,data_0am_train_yy)
    print "train error: " , np.sqrt(np.mean((data_0am_train_predy-data_0am_train_yy)**2))/nom_train
    print "test error: ",  np.sqrt(np.mean((data_0am_test_predy-data_0am_test_y)**2))/nom_test

    dtr = DecisionTreeRegressor(max_depth=5)
    dtr.fit(data_0am_train_xx,data_0am_train_yy)
    data_0am_train_predy = dtr.predict(data_0am_train_xx)
    DTR_train_predy = dtr.predict(data_0am_train_xx)

    data_0am_test_predy = dtr.predict(data_0am_test_x)
    DTR_test_predy = dtr.predict(data_0am_test_x)
    print "DTR report"
    print "train score: ", dtr.score(data_0am_train_xx,data_0am_train_yy)
    print "train error: " , np.sqrt(np.mean((data_0am_train_predy-data_0am_train_yy)**2))/nom_train
    print "test error: ",  np.sqrt(np.mean((data_0am_test_predy-data_0am_test_y)**2))/nom_test


    rng = np.random.RandomState(1)
    abr = AdaBoostRegressor(DecisionTreeRegressor(max_depth=5),
                          n_estimators=300, random_state=rng)
    abr.fit(data_0am_train_xx,data_0am_train_yy)
    data_0am_train_predy = abr.predict(data_0am_train_xx)
    abr_train_predy = abr.predict(data_0am_train_xx)

    data_0am_test_predy = abr.predict(data_0am_test_x)
    abr_test_predy = abr.predict(data_0am_test_x)
    print "ABR report"
    print "train score: ", abr.score(data_0am_train_xx,data_0am_train_yy)
    print "train error: " , np.sqrt(np.mean((data_0am_train_predy-data_0am_train_yy)**2))/nom_train
    print "test error: ",  np.sqrt(np.mean((data_0am_test_predy-data_0am_test_y)**2))/nom_test


    # print lasso_train_predy.shape
    combine_train_predy = np.concatenate((
                                          np.atleast_2d(linear_train_predy),
                                          np.atleast_2d(lasso_train_predy),
                                          np.atleast_2d(DTR_train_predy),
                                          np.atleast_2d(svr_train_predy),
                                          np.atleast_2d(abr_train_predy)),axis=0)
    # print combine_train_predy.shape
    combine_train_predy= np.mean(combine_train_predy,axis=0)
    # print combine_train_predy.shape


    combine_test_predy = np.concatenate((
                                          np.atleast_2d(linear_test_predy),
                                          np.atleast_2d(lasso_test_predy),
                                          np.atleast_2d(DTR_test_predy),
                                          np.atleast_2d(svr_test_predy),
                                          np.atleast_2d(abr_test_predy)),axis=0)
    combine_test_predy= np.mean(combine_test_predy,axis=0)

    print "combine report"
    # print "train score: ", abr.score(data_0am_train_xx,data_0am_train_yy)
    print "train error: " , np.sqrt(np.mean((combine_train_predy-data_0am_train_yy)**2))/nom_train
    print "test error: ",  np.sqrt(np.mean((combine_test_predy-data_0am_test_y)**2))/nom_test