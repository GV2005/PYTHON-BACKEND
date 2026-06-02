from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/employee")
def get_employee():
    return {
        "name": "Venkatesh",
        "age": 25,
        "role": "AI Engineer",
        "city":"salem"
    }