


from datetime import datetime
from typing import Callable, Awaitable, Any, Dict

from beanie import Document
from fastapi import status, Response
from fastapi_pagination import Page, paginate
from pydantic import BaseModel

from src.utils.base.interfaces.model import Model


class BaseApiModel(Model):

    def __init__(
            self,
            document: Callable,
            response: Callable,
            get_document_with_id: Callable
    ):
        self._document = document
        self._response = response
        self._get_document = get_document_with_id

    async def create(
        self,
        body: BaseModel
    ) -> BaseModel:
        document = self._document(
            creation_date=datetime.now(),
            modification_date=datetime.now(),
            **body.dict()
        )
        return await self._response(
            document=await document.insert()
        )

    async def get(
            self,
            _id: str,
            error_message: str
    ) -> BaseModel:
        document = await self._get_document(
            _id=_id,
            document_class=self._document,
            error_message=error_message
        )
        return await self._response(document=document)

    async def put(
            self,
            body: BaseModel,
            _id: str,
            error_message: str,
            set_parameters: Dict[str, Any]
    ) -> BaseModel:
        document = await self._get_document(
            _id=_id,
            document_class=self._document,
            error_message=error_message
        )
        await document.set(set_parameters)
        return await self._response(document=document)

    async def patch(
            self,
            body: BaseModel,
            _id: str,
            error_message: str,
            patch_operation: Callable[[Document], Awaitable]
    ) -> BaseModel:
        document = await self._get_document(
            _id=_id,
            document_class=self._document,
            error_message=error_message
        )
        await patch_operation(document, body)

        document.modification_date = datetime.now()
        await document.save()
        return await self._response(document=document)

    async def list(
            self,
            response: Response
    ) -> Page[BaseModel]:
        documents = await self._document.find_all().to_list()
        documents = [await self._response(document=data) for data in documents]
        return paginate(documents)

    async def delete(
            self,
            _id: str,
            error_message: str
    ) -> Response:
        document = await self._get_document(
            _id=_id,
            document_class=self._document,
            error_message=error_message
        )
        await document.delete()
        return Response(
            status_code=status.HTTP_204_NO_CONTENT
        )
