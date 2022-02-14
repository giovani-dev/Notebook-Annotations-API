import uvicorn
from fastapi import FastAPI
from fastapi_pagination import add_pagination

from src.api.annotation.view import router as annotation
from src.api.notebook.view import router as notebook
from src.conf.connection import Connection


description = """
Welcome to the Notebook Annotations API 🚀🚀🚀

[Base api url](https://notebook-anotations.herokuapp.com)
"""

app = FastAPI(
    title="Notebook Annotations",
    description=description,
    version="0.0.1",
    # terms_of_service="http://example.com/terms/",
    contact={
        "name": "Giovani Liskoski Zanini",
        "url": "https://www.linkedin.com/in/giovani-liskoski-zanini-4a318b180",
        "email": "giovanilzanini@hotmail.com",
    },
    license_info={
        "name": "GNU General Public License v3.0",
        "url": "https://www.gnu.org/licenses/gpl-3.0.html",
    },
)

@app.on_event("startup")
async def startup():
    add_pagination(app)
    await Connection.mongo_db()


app.include_router(annotation)
app.include_router(notebook)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)