from fastapi import FastAPI, Body

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello world!!"}


@app.get("/{user_id}/friends/")
def get_friends(user_id: int):
    return {
        "id": user_id,
        "friends": [
            {
                "id": 2345,
                "bd": None,
                "close_friend": False
            }
        ]
    }


@app.post("/items/")
def create_item(data: dict = Body(...)):
    return {
        "item": data,
    }


# if __name__ == '__main__':
#     uvicorn.run(app)