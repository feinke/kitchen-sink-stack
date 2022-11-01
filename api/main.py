from fastapi import FastAPI
from pytube import YouTube

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World?"}

# https://www.youtube.com/watch?v=1hUQ8O9ufZ0
@app.get("/id/{id}")
async def read_id(id: str):
    yt = YouTube(f'https://youtu.be/{id}')
    if yt:
        streams = yt.streams.filter(only_audio=True)
        return {"streams": streams.all()}
    return {"streams": None}

