from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

# In-memory database
database: Dict[int, dict] = {}

class Item(BaseModel):
    name: str
    description: str

# Create Item
@app.post("/items/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in database:
        raise HTTPException(status_code=400, detail="Item already exists")
    database[item_id] = item.dict()
    return {"message": "Item created", "item": database[item_id]}
@app.get("/")
def home():
    return {"message": "Welcome to my FastAPI app!"}

# Read Item
@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id not in database:
        raise HTTPException(status_code=404, detail="Item not found")
    return database[item_id]

# Update Item
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in database:
        raise HTTPException(status_code=404, detail="Item not found")
    database[item_id] = item.dict()
    return {"message": "Item updated", "item": database[item_id]}

# Delete Item
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in database:
        raise HTTPException(status_code=404, detail="Item not found")
    del database[item_id]
    return {"message": "Item deleted"}
