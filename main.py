import src.extracter as extracter
import src.word_cloud as plot_text

# FAST API Imports
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    url: str


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "Welcome to the webpage article extracter app..."}


@app.post("/extract")
def process_url(item: Item):
    response = extracter.get_text_from_url(item.url)
    plot_text.save_wordcloud(response['content'])
    return response
