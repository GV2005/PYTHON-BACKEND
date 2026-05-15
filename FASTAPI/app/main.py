from routers.get_endp import router
from fastapi import FastAPI

app=FastAPI()
app.include_router(router)