import os
import uvicorn
from fastapi import FastAPI
from db import session
from model import UserTable

# http://localhost:8080/users/static/siddiquee
# http://localhost:8080/users/db/1
app = FastAPI()


@app.get("/users/static/{user_name}")
async def get_user_name(user_name: str):
    return {"user_name": user_name}


@app.get("/users/db/{user_id}")
async def get_user_name(user_id: int):
    user = session.query(UserTable).filter(UserTable.id == user_id).first()
    return user.name


@app.get("/")
async def health_status():
    return {"response": "ok8"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=os.environ.get('PORT'))