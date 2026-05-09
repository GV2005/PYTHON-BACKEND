from fastapi import FastAPI,HTTPException,Request

app=FastAPI()

req_counter={}
max_req=5

@app.get("/data")

def get_data(request:Request):
    client_ip=request.client.host
    req_counter[client_ip]=req_counter.get(client_ip,0)+1


    if req_counter[client_ip]>max_req:
        raise HTTPException(status_code=429,detail="Too many request try again later")
    
    return { "message":f"request {req_counter[client_ip]} successful"}