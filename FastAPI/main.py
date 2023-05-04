from fastapi import FastAPI, status, Response, APIRouter
from enum import Enum
from typing import Optional

from router import blog_get
from router import blog_post
from router import user
from db import models
from db.database import engine


app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)


@app.get('/')
def index():
    return 'Hello world!'

models.Base.metadata.create_all(bind=engine)