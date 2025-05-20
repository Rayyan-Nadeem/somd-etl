import pyodbc
conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=SOHO Database-2013 - CURRENT.accdb.accdb;')
cursor = conn.cursor()
cursor.execute('SELECT * FROM YourTable')
for row in cursor.fetchall():
    print(row)
