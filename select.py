import pandas as pd
import requests
import sqlite3


df = pd.read_csv('https://www.esrl.noaa.gov/psd/enso/mei/data/meiv2.data', header=None) 
print(df )

conn = sqlite3.connect("data.db")
df = pd.read_sql_query("select * from data limit 5", conn)
print (df)
for key,value in df.iteritems():
   print (key,value)


INSERT_QUERY = '''REPLACE INTO data VALUES (?, ?, ?);'''
conn.execute('SELECT * from data').fetchall()
df.to_sql('data', conn, if_exists='append', index=False)
pd.read_sql('select * from data', conn)
# print (d)

# Read first line (to know limits)




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
