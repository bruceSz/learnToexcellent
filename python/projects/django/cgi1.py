#!/usr/bin/env python
from sqlite3  import *
print('Content-Type: text/html\n')
print('<html><head><title>Books</title></head>')
print('<body>')
print("<h1>Books</h1>")
print('ul')
conn=connect('samples.db')
curs.conn.cursor()

curs.execute("create table books(name str)")
curs.execute("select * from books")
for 

print("</ul>")
print('</body></html>')

connection.close()
