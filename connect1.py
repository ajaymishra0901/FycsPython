import mysql.connector as mysql
conn=mysql.connect(user="root",password="scott",host='127.0.0.1')
c=conn.cursor()
c.execute("USE Python3")
c.execute("create table student(eno int(5),ename varchar(20))")
conn.close()
