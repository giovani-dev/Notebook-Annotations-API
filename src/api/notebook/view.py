from __future__ import annotations
from fastapi import Response
from fastapi.routing import APIRouter
from fastapi_pagination import Page
from typing import Optional

from .template import (
    NotebookResponse,
    CreateAndPutNotebookRequest,
    PatchNotebookRequest
)
from .model import Notebook


router = APIRouter(
    prefix="/notebook",
    tags=["schedule"],
)
notebook = Notebook()


@router.post('')
async def create(
    body: CreateAndPutNotebookRequest
) -> NotebookResponse:
    return await notebook.create(body)


@router.get('', response_model=Page[NotebookResponse])
async def list(
        response: Response,
        page: Optional[int] = None,
        size: Optional[int] = None
) -> Page[NotebookResponse]:
    return await notebook.list(response)


@router.get('/{annotation_id}')
async def get(
        annotation_id: str
) -> NotebookResponse:
    return await notebook.get(annotation_id)


@router.put('/{annotation_id}')
async def put(
        annotation_id: str,
        body: CreateAndPutNotebookRequest
) -> NotebookResponse:
    return await notebook.put(body, annotation_id)


@router.patch('/{annotation_id}')
async def patch(
        annotation_id: str,
        body: PatchNotebookRequest
) -> NotebookResponse:
    return await notebook.patch(body, annotation_id)


@router.delete('/{annotation_id}')
async def delete(
        annotation_id: str
) -> Response:
    return await notebook.delete(annotation_id)
