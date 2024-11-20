from datetime import  datetime

from fastapi import  FastAPI
from pydantic import BaseModel



class Item(BaseModel):
    id: int
    name: str
    age: int
    create_at: datetime

fake_db = {}

app = FastAPI()

@app.put("/item/{id}")
def get_item(id:str, item: Item):
    fake_db[id] = item
    print(type(fake_db))
    print(type(fake_db[id]))
    return fake_db

if __name__ == "__main__":
    import  uvicorn
    uvicorn.run(app=app, port=8000)