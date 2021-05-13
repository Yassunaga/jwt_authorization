import traceback

from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.exceptions import RequestValidationError

from starlette.responses import JSONResponse
from starlette.exceptions import HTTPException
from starlette.middleware.cors import CORSMiddleware


from oauth_template.routes import authentication_route
from oauth_template.exceptions import AuthenticationException
from oauth_template.exceptions.user_exeption import InvalidUserException


__version__ = "1.2.0"


app = FastAPI(
    title="Authentication template",
    description="This is an example of the JWT Authentication server", version=__version__
)

app.include_router(authentication_route.router, tags=['Autenticação'])


@app.exception_handler(AuthenticationException)
async def handler_login_exception(requisicao: Request, exception: AuthenticationException):
    return JSONResponse(
        status_code=exception.status_code,
        content={
            "status": exception.status_code,
            "mensagem": exception.message,
            "stacktrace": traceback.format_exc()
        }
    )


@app.exception_handler(InvalidUserException)
async def handler_login_exception(requisicao: Request, exception: InvalidUserException):
    return JSONResponse(
        status_code=exception.status_code,
        headers={"WWW-Authenticate": "Bearer"},
        content={
            "status": exception.status_code,
            "mensagem": exception.message,
            "stacktrace": traceback.format_exc()
        }
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(requisicao: Request, excecao: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={
            "status": 422,
            "mensagem": "Invalid request field",
            "stacktrace": traceback.format_exc()
        }
    )


@app.exception_handler(HTTPException)
async def http_exception_handler(requisicao: Request, excecao: HTTPException):
    mensagem = {404: "Address not found", 405: "Method not allowed", 401: "Invalid Authorization"}
    return JSONResponse(
        status_code=excecao.status_code,
        content={
            "status": excecao.status_code,
            "mensagem": mensagem[excecao.status_code],
            "stacktrace": traceback.format_exc()
        }
    )


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_credentials=True,
    allow_headers=['*']
)
