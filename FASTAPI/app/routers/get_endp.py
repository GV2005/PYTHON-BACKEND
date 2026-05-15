from schemas.emp_basemodel import empbasemodel
from fastapi import APIRouter

router=APIRouter()

@router.get("/employees",response_model=empbasemodel)
def get_employees():
    return {
        "name":"giri",
        "age":21,
        "salary":45000
    }