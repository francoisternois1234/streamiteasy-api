from dotenv import load_dotenv
import os
from fastapi import FastAPI
from livekit import api
import uvicorn

load_dotenv()
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/getToken")
def get_token():
    token = api.AccessToken(os.getenv("LIVEKIT_API_KEY"), os.getenv("LIVEKIT_API_SECRET")) \
        .with_identity("user1") \
        .with_name("User 1") \
        .with_grants(api.VideoGrants(
            room_join=True,
            room="my-room"
        ))
    return {"token": token.to_jwt()}

if __name__ == "__main__":
    uvicorn.run('streamiteasy-api:app', host="0.0.0.0", port=8000, reload=True)