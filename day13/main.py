import psycopg2

conn=psycopg2.connect(
    database="company_db",
    user="postgres",
    password="girig0131@G",
    host="localhost",
    port="5432"
)
cursor=conn.cursor()

cursor.execute('''CREATE TABLE employees1(
               id SERIAL PRIMARY KEY,
               name TEXT NOT NULL,
               salary INTEGER);''')

cursor.execute('''INSERT INTO employees1(name,salary)
               VALUES ('giri',45000),
               ('abi',67000),
               ('sanjay',35000),
               ('albert',49000),
               ('andrya',50000);''')

conn.commit()

cursor.execute('''UPDATE employees1
               SET salary=salary+4500
               WHERE name='giri';''')
conn.commit()

cursor.execute('''DELETE FROM employees1
               WHERE name='andrya';''')
conn.commit()

cursor.execute("SELECT * FROM employees1 ORDER BY id;")
data=cursor.fetchall()
print(data)
conn.close()