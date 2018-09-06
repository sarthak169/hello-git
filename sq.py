import sqlite3 as sq
con = sq.connect('Students.db')
con.close()
# ques 2
con=sq.connect('Students.db')
cur=con.cursor()
query='create table IF NOT EXISTS Students(marks INTEGER, name TEXT);'
cur.execute(query)
con.commit()
l=[]
for i in range(0):

    ab=input('Enter name')
    m=int(input('Enter number'))
    tup=(m,ab)
    l.append(tup)

    if(m>=0 and m<101):
        query="insert into Students(marks,name) values(?,?);"
        cur.executemany(query,l)
        con.commit()
cur.execute("select * from Students")
h=cur.fetchall()
o=80
for marks,name in h:
    if(marks>o):
        print(name)
cur.close()
con.close()
