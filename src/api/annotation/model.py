


from datetime import datetime

from beanie import Document
from fastapi import Response
from fastapi_pagination import Page
from pydantic import BaseModel

from src.api.annotation.utils.response import annotation_response
from src.utils.base.model import BaseApiModel
from src.utils.query import get_document_with_id
from src.db.collections import AnnotationDocument


class Annotation:

    def __init__(self):
        self.base_api_model = BaseApiModel(
            document=AnnotationDocument,
            response=annotation_response,
            get_document_with_id=get_document_with_id,
        )

    @staticmethod
    async def patch_annotation(
            annotation: Document,
            body: BaseModel
    ):
        if body.title:
            annotation.title = body.title
        if body.tags:
            annotation.tags = body.tags

    async def create(
        self,
        body: BaseModel
    ) -> BaseModel:
        return await self.base_api_model.create(body)

    async def get(
        self,
        _id: str
    ) -> BaseModel:
        return await self.base_api_model.get(
            _id=_id,
            error_message="Annotation not found."
        )

    async def put(
        self,
        body: BaseModel,
        _id: str
    ) -> BaseModel:
        return await self.base_api_model.put(
            body=body,
            _id=_id,
            error_message="Annotation not found.",
            set_parameters={
                AnnotationDocument.title: body.title,
                AnnotationDocument.modification_date: datetime.now(),
                AnnotationDocument.tags: body.tags,
            }
        )

    async def patch(
        self,
        body: BaseModel,
        _id: str
    ) -> BaseModel:
        return await self.base_api_model.patch(
            body=body,
            _id=_id,
            error_message="Annotation not found.",
            patch_operation=Annotation.patch_annotation
        )

    async def list(
            self,
            response: Response
    ) -> Page[BaseModel]:
        return await self.base_api_model.list(response)

    async def delete(
            self,
            _id: str
    ):
        return await self.base_api_model.delete(
            _id=_id,
            error_message="Annotation not found."
        )
