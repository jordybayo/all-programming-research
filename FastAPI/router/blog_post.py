from fastapi import APIRouter, Query, Body, Path
from pydantic import BaseModel
from typing import Optional, List, Dict

router = APIRouter(
    prefix="/blog",
    tags=["blog"],
)


class Image(BaseModel):
    url: str
    alias: str


class BlogModel(BaseModel):
    title: str
    body: str
    nb_views: int
    published: Optional[bool]
    tags: List[str] = []
    metadata: Dict[str, str] = None
    image: Optional[Image] = None # complex subtype

@router.post('/new')
def create_blog(blog: BlogModel, id: int, version : int = 1):
    blog.title = blog.title.capitalize()
    return {
        'id': id,
        'version': version,
        'data': blog
    }
  
# VALIDATORS
@router.post('/new/{id}/comment/{comment_id}')
def create_comment(blog: BlogModel,
                   id: int, 
                   comment_title: int = Query(None,  # Parameter data type
                                           title='The id of comment',
                                           description='description comment id',
                                           alias='commentId',
                                           deprecated=True ,
                                           gt=0,
                                           le=1000
                                           ),
                    content: str = Body('Hi how are you', embed=False), # Body data type
                    content2: str = Body(..., embed=True), # Non Optional Body data type #content2: str = Body(Ellipsis, embed=True)
                    min_length: str = Body(..., min_length=10, max_length=50, regex='^a'),
                    # v: Optional[List[str]] = Query(None, alias='version') # multiple values
                    v: Optional[List[str]] = Query(['1.0', '1.1', '1.2'], alias=' version'),
                    comment_id: int = Path(title= 'galere', gt=5, le=35) # Path data type
                   ):
    return {
        'id': id,
        'comment': comment_id,
        'blog': blog
    }
    
    
# require functionalities

def required_functionality():
    return {'message': 'req.FastAPI is important'}