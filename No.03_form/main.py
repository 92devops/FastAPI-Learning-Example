from starlette.requests import Request
from fastapi import  FastAPI,Form
from starlette.templating import Jinja2Templates
from starlette.staticfiles import  StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/login/")
async def login(request: Request):
    return templates.TemplateResponse("file.html", {'request': request})
@app.post("/user/")
async def create_user(request: Request, username: str = Form(...), password: str= Form(...)):
    print(username, password)
    return templates.TemplateResponse("index.html", {'request': request, "username": username, "password": password})



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app=app, host="0.0.0.0", port=8000)
