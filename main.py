from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def greet():
    return "Fastapi learning"

@app.get("/products")
def products():
    return "All the Products"