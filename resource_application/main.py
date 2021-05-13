import uvicorn
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="http://localhost:9080/token",
)


app = FastAPI()


@app.get('/user/image', status_code=200)
def get_user_image(token: str = Depends(oauth2_scheme)):
    return {"status": "authenticated"}


if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=9002)
