from __future__ import annotations
from fastapi import Response, status
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
    """
    ## Description
    * Create one annotation, that you can add in notebook.
    
    ## Body
    * **title**: Title of your annotation.
    * **tags**: List of tags, that is possible to group annotations.

    ## Response
    * **id**: Annotation id
    * **title**: Title of your annotation.
    * **creation_date**: Annotation creation data.
    * **modification_date**: Annotation modification data.
    * **tags**: List of tags, that is possible to group annotations.

    """
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
    """
    ## Description
    * List all annotations with pagination.

    ## Parameters
    * **page**: Page that you want to get. Defaults to 1.
    * **size**: Size of the page that you want to get. Defaults to 1.

    ## Response
    * Code 200
        * **items**: List of annostations.
        * **total**: Total of items.
        * **page**: Page number.
        * **size**: Page size.
    * Code 404
        * **detail**: Error detail.
        * **loc**: Specifies which field the error is in.
        * **msg**: Error message.
        * **type**: Error type.

    """
    return await annotation.list(response)

@router.get(
    '/{annotation_id}',
    response_model=AnnotationResponse
)
async def get(
        annotation_id: str
) -> AnnotationResponse:
    """
    ## Description
    * List annotation detail.

    ## Parameters
    * **annotation_id**: Id of annotation that you need to get.

    ## Response
    * Code 200
        * **id**: Annotation id
        * **title**: Title of your annotation.
        * **creation_date**: Annotation creation data.
        * **modification_date**: Annotation modification data.
        * **tags**: List of tags, that is possible to group annotations.
    * Code 404
        * **detail**: Error detail.
        * **loc**: Specifies which field the error is in.
        * **msg**: Error message.
        * **type**: Error type.

    """
    return await annotation.get(annotation_id)


@router.put(
    '/{annotation_id}',
    response_model=AnnotationResponse
)
async def put(
        annotation_id: str,
        body: CreateAndPutAnnotationRequest
) -> AnnotationResponse:
    """
    ## Description
    * Update all annotation fields.

    ## Parameters
    * **annotation_id**: Id of annotation that you need to put.

    ## Body
    * **title**: Title of your annotation.
    * **tags**: List of tags, that is possible to group annotations.

    ## Response
    * Code 200
        * **id**: Annotation id
        * **title**: Title of your annotation.
        * **creation_date**: Annotation creation data.
        * **modification_date**: Annotation modification data.
        * **tags**: List of tags, that is possible to group annotations.
    * Code 404
        * **detail**: Error detail.
        * **loc**: Specifies which field the error is in.
        * **msg**: Error message.
        * **type**: Error type.
    """
    return await annotation.put(body, annotation_id)


@router.patch(
    '/{annotation_id}',
    response_model=AnnotationResponse
)
async def patch(
        annotation_id: str,
        body: PatchAnnotationRequest
) -> AnnotationResponse:
    """
    ## Description
    * Update annotation with optional fields.

    ## Parameters
    * **annotation_id**: Id of annotation that you need to patch.

    ## Body
    * **title**: Title of your annotation.
    * **tags**: List of tags, that is possible to group annotations.

    ## Response
    * Code 200
        * **id**: Annotation id
        * **title**: Title of your annotation.
        * **creation_date**: Annotation creation data.
        * **modification_date**: Annotation modification data.
        * **tags**: List of tags, that is possible to group annotations.
    * Code 404
        * **detail**: Error detail.
        * **loc**: Specifies which field the error is in.
        * **msg**: Error message.
        * **type**: Error type.
    """
    return await annotation.patch(body, annotation_id)


@router.delete(
    '/{annotation_id}',
    status_code=status.HTTP_204_NO_CONTENT,
    response_description="No content"
)
async def delete(
        annotation_id: str
) -> Response:
    """
    ## Description
    * Delete annotation.

    ## Parameters
    * **annotation_id**: Id of annotation that you need to delete.
    """
    return await annotation.delete(annotation_id)

