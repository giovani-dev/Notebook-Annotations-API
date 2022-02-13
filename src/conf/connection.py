import os

from beanie import init_beanie
import motor

from src.db import models, NotebookDocument


class Connection:

    @staticmethod
    async def mongo_db():
        # NotebookDocument.
        client = motor.motor_asyncio.AsyncIOMotorClient(
            f"mongodb://{os.getenv('MONGO_USER')}:{os.getenv('MONGO_PASSWORD')}@{os.getenv('MONGO_HOST')}" + \
            "/myFirstDatabase?ssl=true&replicaSet=atlas-k4659o-shard-0&authSource=admin&retryWrites=true&w=majority"
        )
        await init_beanie(
            database=client.Annotate_db,
            document_models=models
        )
