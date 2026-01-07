import uvicorn
from fastapi import FastAPI
from src.entrypoints import router
from src.core.config import config


app = FastAPI()
app.include_router(router)


if __name__ == "__main__":
    uvicorn.run(
        app,
        host=config.web.host,
        port=config.web.port
    )