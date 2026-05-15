from fastapi import FastAPI,HTTPException
from fastapi.testclient import TestClient
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
client=TestClient(app)


@app.get("/employees")
def get_employees():

    return {
        "name": "giri"
    }

def test_emp():

    response=client.get("/employees")

    assert response.status_code==200
    assert response.json()["name"]=="giri"

    print("test passed")

if __name__=="__main__":
    test_emp()