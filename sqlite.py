import requests
import sqlite3
import json
import datetime

con = sqlite3.connect("data.db")
cur = con.cursor()


con.commit()
r = requests.get('https://www.esrl.noaa.gov/psd/enso/mei/data/meiv2.data')
# to_db = r.json()
d = json.loads('[]')
dataframe = list()
def data():
  
   date = datetime.datetime.strptime('%Y-%m-%d')
   value = (str(float(row[1-11]),date))
   cur.execute("INSERT INTO data (start_date,end_date ) value (?, ?);",) 
   conn.commit()
# print ("inserted") 


# def display_data(con):
try:
    con = sqlite3.connect("data.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM date ")
except Exception as E:
    print ("Error: ", E)
else:
    for row in cur.fetchall():
        print (row)
con.close() 



# des=data['']
# code=data['start_date']['end_date']['value']
# cur.execute("INSERT INTO date (start_date,end_date ) VALUES (?, ?);",         
# (des,code))
# con.commit()
# con.close()

