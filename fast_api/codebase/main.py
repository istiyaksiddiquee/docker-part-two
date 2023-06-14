import os
import uvicorn
from fastapi import FastAPI

# http://localhost:8083/users/static/siddiquee
PORT=int(os.environ.get('PORT'))

app = FastAPI()

@app.get("/users/static/{user_name}")
async def get_user_name(user_name: str):
    return {"user_name": user_name}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=PORT)