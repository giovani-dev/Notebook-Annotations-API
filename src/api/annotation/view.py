from __future__ import annotations
from fastapi import Response
from fastapi.routing import APIRouter
from fastapi_pagination import Page
from typing import Optional

from .template import (
    AnnotationResponse,
    CreateAndPutAnnotationRequest,
    PatchAnnotationRequest
)
from .model import Annotation


router = APIRouter(
    prefix="/annotation",
    tags=["schedule"],
)
annotation = Annotation()


@router.post('')
async def create(
    body: CreateAndPutAnnotationRequest
) -> AnnotationResponse:
    return await annotation.create(body)


@router.get(
    '',
    response_model=Page[AnnotationResponse]
)
async def list(
        response: Response,
        page: Optional[int] = None,
        size: Optional[int] = None
) -> Page[AnnotationResponse]:
    return await annotation.list(response)

@router.get('/{annotation_id}')
async def get(
        annotation_id: str
) -> AnnotationResponse:
    return await annotation.get(annotation_id)


@router.put('/{annotation_id}')
async def put(
        annotation_id: str,
        body: CreateAndPutAnnotationRequest
) -> AnnotationResponse:
    return await annotation.put(body, annotation_id)


@router.patch('/{annotation_id}')
async def patch(
        annotation_id: str,
        body: PatchAnnotationRequest
) -> AnnotationResponse:
    return await annotation.patch(body, annotation_id)


@router.delete('/{annotation_id}')
async def delete(
        annotation_id: str
) -> Response:
    return await annotation.delete(annotation_id)

