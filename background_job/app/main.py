from jetpack import jetroutine
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def main_function():
    return 200


@app.get("/greet/{name}")
async def index_function(name: str):
    result = await background_task(name)
    return {"result": result}


# This Jetroutine will run as a background job when called
@jetroutine
async def background_task(name: str):
    return "Greetings to {}".format(name)
