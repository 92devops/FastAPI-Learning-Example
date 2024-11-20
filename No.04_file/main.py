import os
import time

from starlette.requests import Request
from fastapi import FastAPI, File, UploadFile, Form
from starlette.templating import Jinja2Templates
from starlette.staticfiles import  StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/upload/")
async def get_files(request: Request):
    return templates.TemplateResponse("file.html", {'request': request})

@app.post("/upload/")
async def file_upload(  username: str=Form(...),file: UploadFile = File(...)):
    start = time.time()
    print(username, "=========")
    try:
        res = await file.read()
        with open("uploads/" + file.filename, "wb") as f:
            f.write(res)
        return {"message": "success", 'time': time.time() - start, 'filename': file.filename, "username": username}
    except Exception as e:
        return {"message": str(e), 'time': time.time() - start, 'filename': file.filename}

    # return templates.TemplateResponse("index.html", {'request': request, "message": f"{name}文件上传成功"})



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app=app, host="0.0.0.0", port=8000)
