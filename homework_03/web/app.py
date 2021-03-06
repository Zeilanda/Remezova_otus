from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello world!"}


@app.get("/ping/")
def get_ping():
    return {
        "message": "pong",
    }
