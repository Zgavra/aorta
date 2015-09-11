__author__ = 'Gavra'

import pyodbc
import json
import collections

connstr = 'DRIVER={SQL Server};SERVER=localhost;DATABASE=fudbal;'
conn = pyodbc.connect(connstr)
cursor = conn.cursor()

cursor.execute("""
            SELECT ID, Grad, Zemlja
            FROM Klubovi
            """)

rows = cursor.fetchall()

# Convert query to row arrays

rowarray_list = []
for row in rows:
    t = (row.ID, row.Ime, row.Zemlja)
    rowarray_list.append(t)

j = json.dumps(rowarray_list)
rowarrays_file = 'klub_rowarrays.js'
f = open(rowarrays_file,'w')
print >> f, j

# Convert query to objects of key-value pairs

objects_list = []
for row in rows:
    d = collections.OrderedDict()
    d['id'] = row.ID
    d['Ime'] = row.Ime
    d['Zip'] = row.Zemlja
    objects_list.append(d)

j = json.dumps(objects_list)
objects_file = 'klub_objects.js'
f = open(objects_file,'w')
print >> f, j

conn.close()