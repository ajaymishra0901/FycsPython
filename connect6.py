import mysql.connector as mysql
conn = mysql.connect(user="root", password="scott",host='127.0.0.1')
c=conn.cursor()
c.execute("use Python3")
c.execute("DROP TABLE STUDENT")
c.execute("SHOW TABLES FROM Python3")
print(c.fetchall())
conn.close()
