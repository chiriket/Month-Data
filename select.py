import pandas as pd
import numpy as np
import requests
import sqlite3
from pandas.tseries.offsets import DateOffset
import datetime

# data extraction

data = pd.read_csv('https://www.esrl.noaa.gov/psd/enso/mei/data/meiv2.data',skiprows =1, sep = '+', header=None)

# create dataframe object
df = pd.DataFrame(data,columns=['YEAR', 'DJ', 'JF', 'FM', 'MA ','AM', 'MJ','JJ','JA','AS','SO','ON', 'ND'])
print (df)

# data transformation
# Replace the placeholder -999 as NaN
df = data.replace(-999.00, np.nan)

# drop irrelevant indexes
data.drop([43,44,])

# time series
date_rng = pd.date_range(start='1/12/1979', end='31/12/2019', freq='2M')
  

# load data
# run sqlite.py to create table
conn = sqlite3.connect('data.db')

conn.set_trace_callback(print)

cursor = conn.cursor()


INSERT_QUERY = '''REPLACE INTO data VALUES (?, ?, ?);'''
conn.execute('SELECT * from data').fetchall()
d = df.to_sql('data', conn, if_exists='append', index=False)
pd.read_sql_query("select * from data limit 5", conn)
print (d)







# def display_data(con):
#     try:
#         con = sqlite3.connect("data.db")
#         cur = con.cursor()
#         cur.execute("SELECT * FROM date ")
#     except Exception as E:
#         print ("Error: ", E)
#     else:
#         for row in cur.fetchall():
#            print (row)
