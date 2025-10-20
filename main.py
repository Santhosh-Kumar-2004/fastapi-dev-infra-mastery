from fastapi import FastAPI

app = FastAPI()

@app.get()
def greet():
    print("Fastapi learning")

greet() 