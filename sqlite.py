# #!/usr/bin/env python3.6
# import requests
# import sqlite3

# import datetime

# con = sqlite3.connect("data.db")
# cur = con.cursor()


# con.commit()
# r = requests.get('https://www.esrl.noaa.gov/psd/enso/mei/data/meiv2.data')
# print(r.text)
# # URL = "https://www.esrl.noaa.gov/psd/enso/mei/data/meiv2.data'"
# # PARAMS = [YEAR, DJ, JF, FM, MA, AM, MJ, JJ, JA, AS, SO, ON, ND ]
# # r = requests.get(url = URL, params = PARAMS) 


# def data():
  
#    date = datetime.datetime.strptime('%Y-%m-%d')
#    value = (str(float(row[1-11]),date))
#    cur.execute("INSERT INTO data (start_date,end_date ) value (?, ?);",) 
#    conn.commit()
# print ("inserted") 


# def showdb():
#    con, cur = opendb()
#    showdb1(cur)
#    con.close()


# # def display_data(con):
# # try:
# #     con = sqlite3.connect("data.db")
# #     cur = con.cursor()
# #     cur.execute("SELECT * FROM date ")
# # except Exception as E:
# #     print ("Error: ", E)
# # else:
# #     for row in cur.fetchall():
# #         print (row)




# # des=data['']
# # code=data['start_date']['end_date']['value']
# # cur.execute("INSERT INTO date (start_date,end_date ) VALUES (?, ?);",         
# # (des,code))
# # con.commit()
# # con.close()

