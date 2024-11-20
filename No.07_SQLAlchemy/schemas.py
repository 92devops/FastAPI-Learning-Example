from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    password: str
    email: str

class UserOut(BaseModel):
    name: str
    email: str