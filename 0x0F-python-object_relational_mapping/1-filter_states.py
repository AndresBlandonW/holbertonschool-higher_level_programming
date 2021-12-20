#!/usr/bin/python3
import MySQLdb
from sys import argv

db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3], port=3306)
cur = db.cursor()
cur.execute("SELECT * FROM states WHERE name LIKE 'N%'")
rows = cur.fetchall()
for row in rows:
    print(row)

cur.close()
db.close()
