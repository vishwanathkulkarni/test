from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# In-memory database
items_db = []

newvalue = "ss"

# Pydantic model for an item
class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float
    quantity: int

@app.post("/items/", response_model=Item)
def create_item(item: Item):
    # Check if item with the same id already exists
    for db_item in items_db:
        if db_item['id'] == item.id:
            raise HTTPException(status_code=400, detail="Item with this ID already exists.")
    
    # Add item to the database
    items_db.append(item.dict())
    return item

@app.get("/items/", response_model=List[Item])
def read_items(skip: int = 0, limit: int = 10):
    return items_db[skip: skip + limit]

@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    for item in items_db:
        if item['id'] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item):
    for index, db_item in enumerate(items_db):
        if db_item['id'] == item_id:
            items_db[index] = item.dict()
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}", response_model=Item)
def delete_item(item_id: int):
    for index, item in enumerate(items_db):
        if item['id'] == item_id:
            deleted_item = items_db.pop(index)
            return deleted_item
    raise HTTPException(status_code=404, detail="Item not found")
