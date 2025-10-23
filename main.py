from fastapi import FastAPI
from models import Product

app = FastAPI()

@app.get("/")
def greet():
    return "Fastapi learning"

products = [
    Product(1, "Laptop", "Laptop gaming", 999, 10),
    Product(2, "Desktop", "Desktop Editing", 499, 20),
    Product(3, "Mobile", "Samsung mobile", 299, 50),
    Product(4, "Ranges", "Cool ranges", 1299, 5)
]

@app.get("/products")
def get_all_products():
    return "All the Products are here!"