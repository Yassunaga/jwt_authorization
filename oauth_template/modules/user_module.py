from typing import Optional
from datetime import timedelta, datetime

from fastapi import Depends
from jose import JWTError, jwt
from pydantic import ValidationError
from passlib.context import CryptContext

from oauth_template.config import ENV
from oauth_template.modules import oauth2_scheme
from oauth_template.modules.database import UserDB
from oauth_template.models.model_user import TokenData
from oauth_template.exceptions.user_exeption import InvalidUserException

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
ALGORITHM = "HS256"


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def generate_password_hash(password):
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, ENV.SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def validate_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, ENV.SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise InvalidUserException
        token_data = TokenData(username=username)
    except (JWTError, ValidationError):
        raise InvalidUserException
    user = UserDB().get_user(username=token_data.username)
    if user is None:
        raise InvalidUserException

    return user


def authenticate(user: str, password: str):
    database_user = UserDB().get_user(user)
    if not database_user:
        raise InvalidUserException

    if not verify_password(password, database_user.hashed_password):
        raise InvalidUserException

    return database_user
