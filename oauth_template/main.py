import uvicorn

from oauth_template import app


if __name__ == "__main__":
    uvicorn.run(app, port=9080)
