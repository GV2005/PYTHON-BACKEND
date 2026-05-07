from fastapi import FastAPI,Form

app=FastAPI()

@app.post("/feedback/")

def feedback(name:str = Form(...),
             email:str=Form(...),
             rating:int =Form(...)):
    return {
        "status":"received successfully",
        "name":name,
        "email":email,
        "Rating":rating
    }