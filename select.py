import pandas as pd
import requests
import sqlite3


df = pd.read_csv('https://www.esrl.noaa.gov/psd/enso/mei/data/meiv2.data', header=None) 
print(df )

conn = sqlite3.connect("data.db")
df = pd.read_sql_query("select * from data limit 5", conn)
print (df)
# for i in df.iteritems():
#     sql = "INSERT INTO `date` (`" +cols + "`) VALUES (" + "%s,"*(len(row)-1) + "%s)"
#     print (i)


INSERT_QUERY = '''REPLACE INTO data VALUES (?, ?, ?);'''
conn.execute('SELECT * from data').fetchall()
d = df.to_sql('data', conn, if_exists='append', index=True)
pd.read_sql('select * from data', conn)
print (d)

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
