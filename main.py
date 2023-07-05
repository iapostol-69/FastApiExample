#
# to start the server run the command: uvicorn main:app
# from your local browser then use this url to access the root: http://localhost:8000
# or to see the api documentation: http://localhost:8000/docs
#
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

