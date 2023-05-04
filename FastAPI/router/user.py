from sqlalchemy.orm import Session

from fastapi import APIRouter, Depends
from schemas import UserBase
from db.database import get_db
from db import db_user


router = APIRouter(
    prefix="/user",
    tags=["user"],
)

# create user
@router.post('/')
def create_user(request: UserBase, db: Depends(get_db)):
    return db_user.create_user(db, request)


# read user 

# update user

# delete user