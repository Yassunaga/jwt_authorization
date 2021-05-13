from pydantic import BaseSettings


class Env(BaseSettings):
    SECRET_KEY: str = "ultra_secreto"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30


ENV = Env()
