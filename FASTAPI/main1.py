from fastapi import FastAPI,Query,Path

emp=[
    {"id":101,"name":"giri","job":"developer"},
    {"id":102,"name":"harish","job":"vibe coder"},
    {"id":103,"name":"arunesh","job":"ai engineer"}
]

app=FastAPI()

@app.post("/display/{name}")

def viewforquery(name:str=Path(min_length=3,max_length=50,regex="^[a-zA-Z]")):
    for e in emp:
        if e["name"].lower()==name.lower():
            return e

@app.post("/display")

def stringquery(name:str=Query(min_length=3,max_length=50,regex="^[a-zA-Z]")):
    for e in emp:
        if e["name"].lower()==name.lower():
            return e

