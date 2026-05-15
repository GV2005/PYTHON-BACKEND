from fastapi import FastAPI,Depends
from datetime import datetime

app=FastAPI()

#functional level :

def db():
    return {"db is connected"}

@app.get("/display")

def display(a:dict=Depends(db)):
    return {"message":"this is from endpoint that","db_status":a}


#class level :

class user:
    def __init__(self):
        self.name="coder"
        self.age=21

def getuser():
    return user()

@app.get("/user-data")

async def get_user(a:user=Depends(getuser)):
    return {"name":a.name,"age":a.age}

#global level :


def ver_tok(tok:str="1234"):
    if tok !="1234":
        raise Exception("Invalid token")
    return True



@app.get("/display")

async def dis():
    return {"message":"hello"}


#sub dependency level:

def gp():
    return {"message":"from grand parent"}

def pa(a:str=Depends(gp)):
    return {f"message : from parents and {a}"}

@app.get("/display")

def child(b:str=Depends(pa)):
    return {"message":b}

#yeild level :

def bb():
    print("book taken from self",datetime.now())
    book="fast api"
    yield book
    print("book returned to shelf",datetime.now())

@app.get("/display")

def tbook(a:str=Depends(bb)):
    return {f"message {datetime.now()}":f"read {a}"}