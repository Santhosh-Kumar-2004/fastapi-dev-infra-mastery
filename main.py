from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def greet():
    return "Fastapi learning"



@app.get("/products")
def get_all_products():
    return "All the Products are here!"