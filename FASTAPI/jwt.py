#jwt=header.payload.signature

from fastapi import FastAPI,HTTPException
from datetime import datetime,timedelta
from jose import jwt,JWTError

#config
ACCESS_TOKEN_EXPIRY_TIME=10
SECRETE_KEY="jgbngkungyiniy768y234"
ALGORITHM="HS256"


def create_token(uname):
    expiry=datetime.utcnow()+timedelta(minutes=ACCESS_TOKEN_EXPIRY_TIME)
    payload={"username":uname,"exptime":expiry.timestamp()}
    return jwt.encode(payload,SECRETE_KEY,ALGORITHM)

def verify_token(token):
    try:
        payload=jwt.decode(token,SECRETE_KEY,algorithms={ALGORITHM})
        return payload["username"]

    except JWTError:
        raise HTTPException(status_code=400,detail="Invalid token")

app=FastAPI()

@app.post("/login")
def user_login(uname:str,password:str):
    if uname=="admin" and password=="1234":
        token=create_token(uname)
        return {"access_token":token}
    return HTTPException(status_code=400,detail="Invalid credentials")


@app.get("/secure_data")
def get_sdata(token:str):
    uname=verify_token(token)
    return {"message":f"hi welcome user {uname} you are accessing secure end point"}

