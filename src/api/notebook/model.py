


from datetime import datetime
from typing import List

from beanie import Document
from fastapi.openapi.models import Response
from fastapi_pagination import Page
from pydantic import BaseModel

from src.api.notebook.utils.response import notebook_response
from src.utils.base.model import BaseApiModel
from src.utils.query import get_document_with_id
from src.db.collections import NotebookDocument, AnnotationDocument


class Notebook:

    def __init__(self):
        self.base_api_model = BaseApiModel(
            document=NotebookDocument,
            response=notebook_response,
            get_document_with_id=get_document_with_id,
        )

    @staticmethod
    async def patch_notebook(
            notebook: Document,
            body: BaseModel
    ):
        if body.description:
            notebook.description = body.description
        if body.annotations:
            notebook.annotations = body.annotations

    @staticmethod
    async def validate_annotations(
            annotations: List[str]
    ):
        for _id in annotations:
            await get_document_with_id(
                _id=_id,
                document_class=AnnotationDocument,
                error_message=f"Annotation {_id} does not exist."
            )

    async def create(
        self,
        body: BaseModel
    ) -> BaseModel:
        await Notebook.validate_annotations(
            body.annotations
        )
        return await self.base_api_model.create(body)

    async def get(
        self,
        _id: str
    ) -> BaseModel:
        return await self.base_api_model.get(
            _id=_id,
            error_message="Notebook not found."
        )

    async def put(
        self,
        body: BaseModel,
        _id: str
    ) -> BaseModel:
        await Notebook.validate_annotations(
            body.annotations
        )
        return await self.base_api_model.put(
            body=body,
            _id=_id,
            error_message="Notebook not found.",
            set_parameters={
                NotebookDocument.description: body.description,
                NotebookDocument.modification_date: datetime.now(),
                NotebookDocument.annotations: body.annotations,
            }
        )

    async def patch(
        self,
        body: BaseModel,
        _id: str
    ) -> BaseModel:
        if body.annotations:
            await Notebook.validate_annotations(
                body.annotations
            )
        return await self.base_api_model.patch(
            body=body,
            _id=_id,
            error_message="Notebook not found.",
            patch_operation=Notebook.patch_notebook
        )

    async def list(
            self,
            response: Response
    ) -> Page[BaseModel]:
        return await self.base_api_model.list(response)

    async def delete(
            self,
            _id: str
    ) -> Response:
        return await self.base_api_model.delete(
            _id=_id,
            error_message="Notebook not found."
        )
