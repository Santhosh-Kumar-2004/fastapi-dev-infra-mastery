from fastapi import FastAPI
from models import Product

app = FastAPI()

@app.get("/")
def greet():
    return "Fastapi learning"

products = [
    Product(id=1, name="Laptop", description="Laptop gaming", price=999, quantity=10),
    Product(id=2, name="Desktop",description="Desktop Editing", price=499, quantity=20),
    Product(id=3, name="Mobile", description="Samsung mobile", price=299, quantity=50),
    Product(id=4, name="Ranges", description="Cool ranges", price=1299, quantity=5)
]

@app.get("/products") #Endpoint for returning all the products
def get_all_products():
    return products