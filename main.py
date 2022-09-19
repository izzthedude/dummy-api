import uvicorn
from fastapi import FastAPI

import coronainfo

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


coronainfo.setup(app)

uvicorn.run(app)
