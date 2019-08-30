import requests
import sqlite3

con = sqlite3.connect("data.db")
cur = con.cursor()


con.commit()
r = requests.get('https://www.esrl.noaa.gov/psd/enso/mei/data/meiv2.data')
to_db = r.json()
des=to_db['start_date']['end_date']['value']
code=to_db['start_date']['end_date']['value']
cur.execute("INSERT INTO date (start_date,end_date ) VALUES (?, ?);",         
(des,code))
con.commit()
con.close()

