import requests
import sqlite3
import json
import datetime

con = sqlite3.connect("data.db")
cur = con.cursor()


con.commit()
r = requests.get('https://www.esrl.noaa.gov/psd/enso/mei/data/meiv2.data')
# to_db = r.json()
data = json.loads('{}')
# url = requests.get('https://www.esrl.noaa.gov/psd/enso/mei')
# content = requests.get(url).content
# dataset = json.loads(content)
# dataframe=list()
des=data['start_date']['end_date']['value']
code=data['start_date']['end_date']['value']
cur.execute("INSERT INTO date (start_date,end_date ) VALUES (?, ?);",         
(des,code))
con.commit()
con.close()

