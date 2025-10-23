from fastapi import FastAPI
from models import Product

app = FastAPI()

@app.get("/")
def greet():
    return "Fastapi learning"

products = [
    Product("1")
]

@app.get("/products")
def get_all_products():
    return "All the Products are here!"