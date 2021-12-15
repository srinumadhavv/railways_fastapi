from fastapi import FastAPI
from .routers import user

app=FastAPI()

app.include_router(user.router)

@app.get("/") #path operation
def root():
    return{"message":"Hello World!!"}