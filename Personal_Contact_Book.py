import sqlite3

conn = sqlite3.connect('contact_book')
c = conn.cursor()
c.execute("SELECT * FROM 'contact_book' ORDER BY name")

data = c.fetchall()
print(data)


