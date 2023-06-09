from db.database import Base
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy import Column

class DbUser(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)