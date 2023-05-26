import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='root', password='Heisenberg_123')
# print(mydb)

mycursor = mydb.cursor()
# mycursor.execute('CREATE DATABASE mydb_python')
# mycursor.execute('SHOW databases')
# for x in mycursor:
#     print(x)

mycursor.execute('USE mydb_python')
# mycursor.execute('CREATE TABLE employee(name VARCHAR(250), dept VARCHAR(250), salary INT);')
# mycursor.execute('SHOW TABLES')
# for x in mycursor:
#     print(x)

# sql = "INSERT INTO employee VALUES('CHANDLER', 'SALES', 250000)"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount, "record inserted")

"""inserting multiple values"""

# sql = 'INSERT INTO employee(name, dept, salary) VALUES(%s, %s, %s)'
# val = [
#     ('Joey', 'python', 125000),
#     ('Monica', 'java', 130000),
#     ('phoebe', 'cyber security', 160000)
# ]
# mycursor.executemany(sql, val)
# mydb.commit()
# print(mycursor.rowcount, 'records inserted')

# mycursor.execute('SELECT * FROM employee')
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)

# print(myresult)

# myresult2 = mycursor.fetchone()
# print(myresult2)

# mycursor.execute("SELECT * FROM employee WHERE dept='python'")
# myresult3 = mycursor.fetchone()
# print(myresult3)

# delete = "DELETE FROM employee WHERE name='CHANDLER'"
# mycursor.execute(delete)
# mydb.commit()
# print(mycursor.rowcount, 'records deleted')

# sql = 'INSERT INTO employee(name, dept, salary) VALUES(%s, %s, %s)'
# val = [
#     ('chandler', 'cpp', 140000),
#     ('Rachel', 'testing', 120000),
#     ('Ross', 'devops', 115000)
# ]
# mycursor.executemany(sql, val)
# mydb.commit()
# print(mycursor.rowcount, 'values inserted')

# sql = "UPDATE employee SET dept='c' WHERE name='chandler'"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount, 'values updated')

# mycursor.execute('SELECT * FROM employee')
# x = mycursor.fetchall()
# for i in x:
#     print(i)

"""order by asc"""
# mycursor.execute('SELECT * FROM employee ORDER BY salary DESC')
# x = mycursor.fetchall()
# for i in x:
#     print(i)

"""order by desc"""
mycursor.execute('SELECT * FROM employee ORDER BY salary ASC')
x = mycursor.fetchall()
for i in x:
    print(i)

"""distinct"""
# mycursor.execute('SELECT DISTINCT name FROM employee')
# x = mycursor.fetchall()
# for i in x:
#     print(i)

# mycursor.execute('CREATE TABLE Job(dept VARCHAR(250), head VARCHAR(250), branch VARCHAR(250))')
# sql = 'INSERT INTO Job(dept, head, branch) VALUES(%s, %s, %s)'
# val = [
#     ('python', 'John', 'NY'),
#     ('c', 'Watson', 'LA'),
#     ('cyber security', 'Root', 'PH'),
#     ('java', 'carley', 'CL'),
#     ('testing', 'Jamie', 'CN'),
#     ('devops', 'Hart', 'DT')
# ]
# mycursor.executemany(sql, val)
# mydb.commit()
# print(mycursor.rowcount, 'rows added')
# x = mycursor.fetchall()
# for i in x:
#     print(i)

# mycursor.execute('ALTER TABLE employee ADD emp_id AUTO INCREMENT PRIMARY KEY')

"""
relationship queries
--------------------
one to one: 
    user --> password
one to many:
    class --> students
many to many:
    students --> courses
many to one:
    students --> class
"""
