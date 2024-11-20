from fastapi import FastAPI,Form

import schemas

app = FastAPI()

# @app.post("/item/", response_model=schemas.ItemOut)
@app.post("/item/", response_model=schemas.Item, response_model_exclude={"password"})
async def create_item( item: schemas.Item):
    return item

items = {
    "foo": {"name": "aaa", "email": "aaa@qq.com"},
    "bar": {"name": "bbb", "email": "bbb@qq.com"}
}

@app.get("/item/{item_name}",  response_model=schemas.ItemOut, response_model_exclude_unset=False)
async def get_item_by_name(item_name: str):
    return items[item_name]

if __name__ == "__main__":
    import  uvicorn
    uvicorn.run(app=app, port=8000)