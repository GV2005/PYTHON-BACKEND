import sqlite3
conn=sqlite3.connect("company.db")
cursor=conn.cursor()

#showing employees
cursor.execute('''SELECT * FROM employees''')
data=cursor.fetchall()
print(data)

#add employee
cursor.execute('''INSERT INTO employees(name,salary)
               VALUES ('prasath',34567);''')
conn.commit()

#update salary
cursor.execute('''UPDATE employees
               SET salary = salary + 3456;''')
conn.commit()

#delete employee
cursor.execute('''DELETE FROM employees
               WHERE name='alex';''')
conn.commit()

#final updated database
cursor.execute('''SELECT * FROM employees''')
data=cursor.fetchall()
print(data)

conn.close()