from getpass import getpass
import cPickle as pickle
import pandas as pd
import time
import mysql.connector
from matplotlib import pyplot
import pickle
import os
import numpy as np
import math

def modelBuilder(sql_db,uniqueness_T):
    # usr = raw_input("Username: ")
    # passw = getpass()
    # cnx = mysql.connector.connect(user=usr, password=passw,
    #                               host='127.0.0.1',
    #                               database=sql_db)
    # df = pd.read_sql('SELECT * FROM fpData', con=cnx)
    # all_columns = df.columns.tolist()
    # # irrelevant_params = ['octaneScore', 'sunspiderTime', 'timezoneJS', 'id', 'counter', 'time']
    # # octaneScore, sunspiderTime, timezoneJS, id, counter, time
    # print "List of attributes in the dataset:\n", ', '.join(all_columns)
    #
    # irrelevant_params = ['id', 'time', 'timezoneJS', 'octaneScore', 'sunspiderTime','counter','addressHttp']
    # start = time.time()
    # # q = df.drop(['id', 'counter', 'addressHttp'], axis=1)
    # q = df.drop(['id', 'counter'], axis=1)
    # x = q.to_string(header=False, index=False, index_names=False).split('\n')
    # vals = [''.join(ele.split()) for ele in x]
    # all_counts = [vals.count(fing) for fing in list(set(vals))]
    # with open('objs.pkl', 'w') as f:
    #     pickle.dump(all_counts,f)

    with open('objs.pkl', 'r') as f:
        all_counts = pickle.load(f)
    x_axis = list(set(all_counts))
    y_axis = [all_counts.count(xx) for xx in x_axis]
    print ([xx for xx in x_axis])
    print ([xx for xx in y_axis])

    pyplot.bar(x_axis,y_axis)
    pyplot.xticks(range(1,40,2),range(1,40,2))
    # pyplot.hist(all_counts)
    pyplot.show()
    # final_result = {col:{} for col in all_columns if col not in irrelevant_params}
    # value_counts = {colum:df[colum].value_counts() for colum in all_columns if colum not in irrelevant_params}

    end = time.time()
    # print "Model with uniqueness threshold of %d was built in %d seconds."%(uniqueness_T,end-start)

if __name__ == '__main__' :
    modelBuilder('amiunique',3)