from fastapi import FastAPI

app=FastAPI()

@app.get("/") #path operation
def root():
    return{"message":"Hello World!!"}

