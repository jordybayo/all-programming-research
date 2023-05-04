from fastapi import FastAPI, status, Response, APIRouter
from enum import Enum
from typing import Optional
from router import blog_get
from router import blog_post


app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)


@app.get('/')
def index():
    return 'Hello world!'

# path parameters
@app.get('/items/all')
def read_items():
    return {'items': 'all'}

@app.get('/items/{item_id}')
def read_item(item_id):
    return {'item_id': item_id}

