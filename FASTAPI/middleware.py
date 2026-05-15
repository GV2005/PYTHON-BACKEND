from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
import psycopg2
import time

conn=psycopg2.connect(
    database="company_db",
    user="postgres",
    password="girig0131@G",
    host="localhost",
    port="5432"
)
cursor=conn.cursor()

app=FastAPI()

@app.get("/employees")

def get_employees():
    try:
        cursor.execute("SELECT * FROM employees1;")
        rows=cursor.fetchall()
        return [{"id":row[0],"name":row[1]} for row in rows]
    except HTTPException as e:
        raise HTTPException(status_code=400,detail=f"unable to get data {e}")

@app.middleware("/employees")

async def middleware_name(request,call_next):
    a=time.time()
    response=await call_next(request)
    b=time.time()
    print(f"{request.url.path} ----> {b-a}")
    return response