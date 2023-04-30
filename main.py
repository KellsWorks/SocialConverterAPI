from typing import Union
from fastapi import FastAPI
from app.facebook.main import Facebook

from app.youtube.main import Youtube

app = FastAPI()

youtube = Youtube()
facebook  = Facebook()

@app.get("/")
def read_root():
    return {"Server": "Running..."}

@app.get("/convert/youtube/video")
def get_response(url: Union[str, None] = None):
    
    return youtube.convert(url)

@app.get("/convert/facebook/video")
def get_response(url: Union[str, None] = None):

    return facebook.convert(url=url)
