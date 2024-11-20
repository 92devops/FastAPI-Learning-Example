from typing import List

from fastapi import FastAPI, Depends,HTTPException
from sqlalchemy.orm import Session
from starlette import status
import models
from database import engine, get_db
import schemas
import utils

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/user", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
async  def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    try:
        hashed_password = utils.hash(user.password)
        user.password = hashed_password

        new_user = models.User(**user.dict())
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    except Exception as e:
        print(e)
        raise  HTTPException(status_code=status.HTTP_403_FORBIDDEN, headers={"X-error": "this is a error"},  detail=f"数据错误{e}")

@app.get("/user", status_code=status.HTTP_200_OK, response_model=List[schemas.UserOut])
async  def get_user(db: Session = Depends(get_db)):
    usrs =  db.query(models.User).all()
    return usrs


if __name__ == "__main__":
    import  uvicorn
    uvicorn.run(app=app, port=8000)