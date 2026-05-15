from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
import psycopg2

conn=psycopg2.connect(
    database="company_db",
    user="postgres",
    password="girig0131@G",
    host="localhost",
    port="5432"
)
cursor=conn.cursor()

class EmployeeResponse(BaseModel):
    id:int
    name:str

app=FastAPI()

@app.get("/employees",response_model=list[EmployeeResponse])

def get_employees():
    try:
        cursor.execute("SELECT * FROM employees1;")
        rows=cursor.fetchall()
        return [{"id":row[0],"name":row[1]} for row in rows]
    except HTTPException as e:
        raise HTTPException(status_code=400,detail=f"unable to get data {e}")

@app.post("/employees",status_code=201)

def add_employees(name:str,salary:int):
    try:
        cursor.execute('''INSERT INTO employees1(name,salary)
                       VALUES (%s,%s);''',(name,salary))
        conn.commit()
        return {
            "message": "employee added successfully"
        }
    
    except Exception as e:
        raise HTTPException(status_code=400,detail=f"unable to insert data {e}")
