import pandas as pd
import numpy as np
import requests
import sqlite3


df = pd.read_csv('https://www.esrl.noaa.gov/psd/enso/mei/data/meiv2.data', header=None) 

df.replace(-999.00, np.nan, inplace=True) 
# date_rng = pd.date_range(start='1/12/1979', end='31/12/2019', freq='2M')

# for ind, column in enumerate(df.columns):
#     print(ind, column)

conn = sqlite3.connect("data.db")
pd.read_sql_query("select * from data limit 5", conn)
print (df)


for key,value in df.iteritems():
   print (key,value)


INSERT_QUERY = '''REPLACE INTO data VALUES (?, ?, ?);'''
conn.execute('SELECT * from data').fetchall()
d = df.to_sql('data', conn, if_exists='append', index=False)
pd.read_sql('select * from data', conn)
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
