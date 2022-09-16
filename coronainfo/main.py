from pathlib import Path

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/worldometer")
async def worldometer():
    content = ""
    path = Path(__file__).parent / "static" / "worldometer.html"
    with open(path, "r") as file:
        content = file.read()
        content = " ".join(content.split())

    return {"html": content}


uvicorn.run(app)
