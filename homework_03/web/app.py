from fastapi import FastAPI, Body

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello world!!!"}


@app.post("/ping/")
def create_item(data: dict = Body(...)):
    return {
        "message": "pong",
    }
