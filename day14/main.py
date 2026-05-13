from fastapi import FastAPI,HTTPException
import psycopg2

app=FastAPI()
conn=psycopg2.connect(
    database="company_db",
    user="postgres",
    password="girig0131@G",
    host="localhost",
    port="5432"
)
cursor=conn.cursor()


@app.get("/employees")

def get_employees():
    try:
        cursor.execute("SELECT * FROM employees;")
        data=cursor.fetchall()
        return {"datas":data}
    except Exception as e:
        return {"error":f'unable to get bcz {e}'}


@app.post("/addemployee")

def add_employees(name:str,salary:int):
    try:
        cursor.execute("INSERT INTO employees(name,salary) VALUES (%s,%s)",(name,salary))
        conn.commit()
        return {"message":"inserted successfully"}
    except Exception as e:
        return {"message":f'unable to insert data bcz {e}'}
    
@app.patch("/update_employee/{id}")

def update_employees(id:int):
    try:
        cursor.execute('''UPDATE employees
                       SET salary=salary + 5790
                       WHERE id=%s''',(id,))
        conn.commit()
        return {"message":"updated successfully"}
    except Exception as e:
        return {"message":f'unable to update data bcz {e}'}


@app.delete("/delete_employee/{id}")

def delete_employees(id:int):
    try:
        cursor.execute('''DELETE FROM employees
                       WHERE id=%s''',(id,))
        conn.commit()
        return {"message":"DELETED successfully"}
    except Exception as e:
        return {"message":f'unable to update data bcz {e}'}

