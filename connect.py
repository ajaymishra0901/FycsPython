import mysql.connector as mysql
conn=mysql.connect(user="root",password="scott",host='localhost')
c=conn.cursor()
c.execute("CREATE DATABASE Python3")
conn.close()
