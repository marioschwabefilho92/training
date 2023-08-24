import mysql.connector

dbconfig = { 'host': '127.0.0.1',
             'user': 'vsearch',
             'password': 'mario',
             'database': 'vsearchlogDB',}

conn = mysql.connector.connect(**dbconfig)
cursor = conn.cursor()

_SQL = """insert into log
          (phrase, letters, ip, browser_string, results)
          Values
          (%s, %s, %s, %s, %s)"""
cursor.execute(_SQL)
res = cursor.fetchall()
for row in res:
    print(row)

conn.commit()
_SQL = """select * from log"""
cursor.execute(_SQL)
for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()