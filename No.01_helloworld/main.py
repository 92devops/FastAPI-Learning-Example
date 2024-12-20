from  fastapi import  FastAPI

app = FastAPI()

@app.get("/")
async def main():
    return {"message": "hello FastAPI."}

if __name__ == "__main__":
    import  uvicorn
    uvicorn.run(app=app, host="127.0.0.1", port=8000)