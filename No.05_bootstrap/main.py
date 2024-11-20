from fastapi import FastAPI,Form
from starlette.requests import Request
from starlette.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.post("/login")
async def login(request: Request, username: str= Form(...), password: str=Form(...)):
    return templates.TemplateResponse("index.html", {"request": request, "username": username, "password": password})

@app.get("/login")
async def login_show(request: Request):
    return templates.TemplateResponse("signin.html", {"request": request})


if __name__ == "__main__":
    import  uvicorn
    uvicorn.run(app=app, port=8000)