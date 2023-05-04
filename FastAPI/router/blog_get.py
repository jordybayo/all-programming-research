from fastapi import FastAPI, status, Response, APIRouter, Depends
from enum import Enum
from typing import Optional

from router.blog_post import required_functionality


router = APIRouter(
    prefix="",
    tags=["blog"],
)

class blogType(str, Enum):
    tech = 'tech'
    health = 'health'
    sports = 'sports'

# query parameters

@router.get(
        '/all',
        tags=['blog'],
        summary="get blogs details",
        description="Get blog details with pagination"
    )
def get_blogs(page=1, page_size: Optional[int] = None, req_paramaeter: dict = Depends(required_functionality)):
    return {'message ': f'{page_size} blogs on page {page}', 'req': f'{req_paramaeter}'}

@router.get('/{id}/comment/{comment_id}',
        tags=['blog'],
        summary="get blogs details",
        description="Get blog details with pagination"
    )

def get_complex_blog(page=1, page_size: Optional[int] = None):
    return {'message ': f'{page_size} blogs on page {page}'}

@router.get('/type/{type}', tags=['blog'])
def get_blog_Type(type: blogType):
    return {'message ': f'blog type {type}'}


# status code
@router.get('/{id}', status_code=status.HTTP_200_OK, tags=['blog'])
def get_blog(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_200_OK
        return {'message': 'blog found'}
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': 'blog not found'}
