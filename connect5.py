import mysql.connector as mysql
conn = mysql.connect(user="root", password="scott",host='127.0.0.1')
c=conn.cursor()
c.execute("USE Python3")
c.execute("select * from student")
rows=c.fetchall()
stuid=rows[1][0]
print(stuid)
c.execute("update student set ename = 'MITALIVIS' where eno = "+str(stuid))
conn.commit
c.execute("select * from STUDENT")
print(c.fetchall())
conn.close()


