from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    quantity: int
    
    def __init__(self, id: int, name: str, description: str, price: float, quantity: int, **data):
        if price < 0:
            raise ValueError("price must be non-negative")
        if quantity < 0:
            raise ValueError("quantity must be non-negative")
        super().__init__(id=id, name=name, description=description, price=price, quantity=quantity, **data)