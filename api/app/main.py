from fastapi import FastAPI
from jetpack import jetroutine
from typing import Dict, Any
import uvicorn


app = FastAPI()
 

@app.get("/")
async def root() -> Dict[str, str]:
    return {"message": "Hello World!"}


@app.get("/launch_job/{msg}")
async def launch_job(msg: str) -> Dict[str, Any]:
    result = await background_job(msg)
    return {"message": result}


@jetroutine
async def background_job(msg: str) -> str:
    return msg.capitalize()


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080)
