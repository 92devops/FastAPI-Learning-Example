from typing import List

from pydantic import BaseModel

class Item(BaseModel):
    name: str
    password: str
    email: str

class ItemOut(BaseModel):
    name: str
    email: str