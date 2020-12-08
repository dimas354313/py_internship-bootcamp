#sqlitedatabase.py
import sqlite3
import day12
import json

conn = sqlite3.connect('day12.db')
print("Opened database successfully");
c=conn.cursor()
c.execute('''CREATE TABLE PROFILE1(data json);''')
print("Table created successfully");
c.execute('''INSERT INTO PROFILE1 VALUES(?)''',(json.dumps(day12.x),))
c.execute('''SELECT * FROM PROFILE1''')
print(c.fetchall())
conn.commit()
c.close()