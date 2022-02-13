from abc import ABC, abstractmethod
from typing import Dict, Any, Callable, Awaitable

from fastapi.openapi.models import Response
from pydantic import BaseModel


class Model(ABC):

    @abstractmethod
    async def create(
            self,
            body: BaseModel
    ) -> BaseModel: ...

    @abstractmethod
    async def get(
            self,
            _id: str,
            error_message: str
    ) -> BaseModel: ...

    @abstractmethod
    async def put(
            self,
            body: BaseModel,
            _id: str,
            error_message: str,
            set_parameters: Dict[str, Any]
    ) -> BaseModel: ...

    @abstractmethod
    async def patch(
            self,
            body: BaseModel,
            _id: str,
            error_message: str,
            patch_operation: Callable[[], Awaitable]
    ) -> BaseModel: ...

    @abstractmethod
    async def list(
            self,
            response: Response
    ) -> BaseModel: ...

    @abstractmethod
    async def delete(
            self,
            _id: str,
            error_message: str
    ) -> Response: ...
