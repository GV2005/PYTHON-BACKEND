from fastapi import FastAPI,Response,Cookie,HTTPException
from uuid import uuid4
from typing import Optional
from datetime import datetime,timedelta


app=FastAPI()

couname="admin"
copass="1234"

sessions={}
time=10

@app.post("/login")

def login(uname:str,pas:str,res:Response):
    if couname==uname and copass==pas:
        sid=str(uuid4())
        cur_time=datetime.now()
        exp_time=cur_time+timedelta(seconds=time)
        sessions[sid]={"username":uname,"exp_time":exp_time}
        res.set_cookie(key="sid",value=sid,httponly=True,max_age=time)

        return {"message":"login success"}
    
    else:
        raise HTTPException(status_code=401,detail="Invalid credentials")

@app.get("/home")

def home(sid:Optional[str]=Cookie(None)):
    if sid is None or sid not in sessions:
        raise HTTPException(status_code=401,detail="Not authorised")
    session_data=sessions[sid]

    if session_data["exp_time"]<datetime.now():
        sessions.pop(sid)
    
    return {"data":sessions}
