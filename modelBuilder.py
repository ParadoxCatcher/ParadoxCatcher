import mysql.connector
# from itertools import combinations
from getpass import getpass
import cPickle as pickle
import pandas as pd
import time

def modelBuilder(sql_db,uniqueness_T,file_name):
    usr = raw_input("Username: ")
    passw = getpass()
    cnx = mysql.connector.connect(user=usr, password=passw,
                                  host='127.0.0.1',
                                  database=sql_db)
    df = pd.read_sql('SELECT * FROM fpData', con=cnx)
    all_columns = df.columns.tolist()
    # irrelevant_params = ['octaneScore', 'sunspiderTime', 'timezoneJS', 'id', 'counter', 'time']
    # octaneScore, sunspiderTime, timezoneJS, id, counter, time
    print "List of attributes in the dataset:\n", ', '.join(all_columns)

    params = raw_input("Please input the irrelevant parameters in the dataset separated by a comma or press "
                                  "Enter to continue:")
    irrelevant_params = []
    if params != '':
        tmp_params = params.split(',')
        for param in tmp_params:
            param = param.strip()
            assert param in all_columns, "The parameter %s doesn't exist in the dataset." %param
            irrelevant_params.append(param)
    start = time.time()
    final_result = {col:{} for col in all_columns if col not in irrelevant_params}
    value_counts = {colum:df[colum].value_counts() for colum in all_columns if colum not in irrelevant_params}
    for col_idx,col1 in enumerate(all_columns):
        if col1 not in irrelevant_params:
            print "%f%% of columns are done..."%((col_idx*100)/len(all_columns))
            other_columns = all_columns[:]
            other_columns.remove(col1)
            val_counts1 = value_counts[col1]
            final_result[col1] = {}
            for value_idx1, freq1 in enumerate(val_counts1):
                if freq1 >= uniqueness_T:
                    current_value1 = val_counts1.keys()[value_idx1]
                    df_value_indices = df[df[col1] == val_counts1.keys()[value_idx1]].index
                    final_result[col1][current_value1] = {}
                    final_result[col1][current_value1]['__probability'] = float(freq1)/val_counts1.sum()
                    for col2 in other_columns:
                        if col2 not in irrelevant_params:
                            final_result[col1][current_value1][col2] = {}
                            val_counts2 = df[col2][df_value_indices].value_counts()
                            for value_idx2, freq2 in enumerate(val_counts2):
                                if freq2 >= uniqueness_T:
                                    current_value2 = val_counts2.keys()[value_idx2]
                                    final_result[col1][current_value1][col2][current_value2] = {}
                                    final_result[col1][current_value1][col2][current_value2]['__probability'] = float(freq2)/val_counts2.sum()
    end = time.time()
    print "Model with uniqueness threshold of %d was built in %d seconds."%(uniqueness_T,end-start)
    with open(file_name, 'wb') as fb:
        pickle.dump(final_result, fb, pickle.HIGHEST_PROTOCOL)
