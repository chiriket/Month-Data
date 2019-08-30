import os
import requests
import sqlite3

DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'database.sqlite3')

def db_connect(db_path=DEFAULT_PATH):
    con = sqlite3.connect(db_path)
    return con

con = sqlite3.connect("data.db")
cur = con.cursor()


# cur.execute("INSERT INTO date VALUES (" ")
# for row in cur.execute('SELECT * FROM stocks ORDER BY price'):
#         print(row)

# Save (commit) the changes
con.commit()
r = requests.get('https://www.esrl.noaa.gov/psd/enso/mei/data/meiv2.data')
to_db = r.json()
des=to_db['start_date']['end_date']['value']
code=to_db['start_date']['end_date']['value']
cur.execute("INSERT INTO date (start_date,end_date ) VALUES (?, ?);",         
(des,code))
con.commit()
con.close()

