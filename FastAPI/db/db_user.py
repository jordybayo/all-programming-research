from sqlalchemy.orm.session import Session

from schemas import UserBase
from db.models import DbUser
from db.hash import Hash

def create_user(db: Session, request: UserBase):
    db_user = DbUser(
        username=request.username,
        email=request.email,
        password=Hash(request.password)
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user