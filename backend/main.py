from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
import uvicorn

app = FastAPI()


class CreateUser(BaseModel):
    email: EmailStr


@app.get("/items/")
def list_items():
    return [
        "item1",
        "item2"
    ]


@app.get("/helo/")
def hello(name: str = "noname"):
    name = name.strip().title()
    return {"message": f"hello {name}"}


@app.post("/users/")
def create_user(user: CreateUser):
    return {"email": user.email}


@app.get("/items/{item_id}/")
def get_item(item_id: int):
    return {
        "item": item_id,
    }


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
