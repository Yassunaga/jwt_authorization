class AuthenticationException(Exception):
    def __init__(
            self,
            message: str = "Internal Error",
            status_code: int = 500,
            stacktrace: str = None
    ):
        self.message = message
        self.status_code = status_code
        self.stacktrace = stacktrace
