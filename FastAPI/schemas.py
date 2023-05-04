from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    email: str
    full_name: str = None