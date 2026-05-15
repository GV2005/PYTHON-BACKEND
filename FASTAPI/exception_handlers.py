from fastapi import FastAPI,HTTPException
from fastapi.responses import JSONResponse
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

app=FastAPI()

class employeeoutput(BaseModel):
    id:int
    name:str

@app.get("/employees",response_model=list[employeeoutput])
def get_employees():

    cursor.execute("SELECT * FROM employees1;")
    rows=cursor.fetchall()

    if not rows:
        raise HTTPException(status_code=404,detail="employees not found")
    
    return [{"id":row[0],"name":row[1]} for row in rows]
    
@app.exception_handler(HTTPException)
async def handler(request,exc):
     return JSONResponse(
        status_code=exc.status_code,
        content={
            "custom_error": exc.detail
        }
     )