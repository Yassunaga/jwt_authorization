from pydantic import BaseModel
from typing import Optional


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


class User(BaseModel):
    username: str
    hashed_password: str
    email: Optional[str] = None
    full_name: Optional[str] = None

    def __iter__(self):
        yield 'username', self.username
        yield 'hashed_password', self.hashed_password
        yield 'email', self.email
        yield 'full_name', self.full_name
