from fastapi import status
from oauth_template.exceptions import AuthenticationException


class InvalidUserException(AuthenticationException):
    def __init__(
            self,
            message="Invalid User",
            status_code: int = status.HTTP_401_UNAUTHORIZED
    ):
        super().__init__(message, status_code)
