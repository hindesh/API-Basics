from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/") # decorator to define a GET endpoint at the root URL
def read_root():
    return {"message": "API is alive!"}

@app.get("/about")
def about():
    return {"name": "API-ONE", 
            "version": "1.0.0",
            "author": "Akash"
            }

@app.get("/greet")
def greet(name: str, age: int):
    return {
        "message": f"Hello {name}, how are you?",
        "is_adult": age >= 18
    }


# This defines the shape of incoming data
class PredictionInput(BaseModel):
    feature1: float
    feature2: float
    feature3: float

@app.post("/predict")
def predict(input: PredictionInput):
    # For now just echo it back — we'll add the real model next
    return {
        "received": input,
        "sum": input.feature1 + input.feature2 + input.feature3
    }
