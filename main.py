from fastapi import FastAPI

app = FastAPI()

def greet():
    print("Fastapi learning")

greet()