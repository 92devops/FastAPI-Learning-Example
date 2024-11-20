from starlette.requests import Request
from fastapi import FastAPI
from starlette.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def main(request: Request):
    return templates.TemplateResponse("base.html", {"request": request, "message": "Hello world"})


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app=app, host="0.0.0.0", port=8000)