import uvicorn
from fastapi import FastAPI
from fastapi_pagination import add_pagination

from src.api.annotation.view import router as annotation
from src.api.notebook.view import router as notebook
from src.conf.connection import Connection

app = FastAPI()


@app.on_event("startup")
async def startup():
    add_pagination(app)
    await Connection.mongo_db()


app.include_router(annotation)
app.include_router(notebook)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)