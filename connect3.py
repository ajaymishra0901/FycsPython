import mysql.connector as mysql
conn=mysql.connect(user="root",password="scott",host='127.0.0.1')
c=conn.cursor()
c.execute("show tables from Python3")
print(c.fetchall())
conn.close()
