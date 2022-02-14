from __future__ import annotations
from fastapi import Response, status
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
    """
    ## Description
    * Create one notebook, that you can relate with annotation.

    ## Body
    * **description**: Description of your annotation.
    * **annotations**: List of annotation ID that will be related.

    ## Response
    * Code 200
        * **id**: Notebook id
        * **description**: Notebook description.
        * **creation_date**: Notebook creation data.
        * **modification_date**: Notebook modification data.
        * **annotations**: List of annotation id that was related.
    * Code 404
        * **detail**: Error detail.
        * **loc**: Specifies which field the error is in.
        * **msg**: Error message.
        * **type**: Error type.
    """
    return await notebook.create(body)


@router.get('', response_model=Page[NotebookResponse])
async def list(
        response: Response,
        page: Optional[int] = None,
        size: Optional[int] = None
) -> Page[NotebookResponse]:
    """
    ## Description
    * List all notebooks with pagination.

    ## Parameters
    * **page**: Page that you want to get. Defaults to 1.
    * **size**: Size of the page that you want to get. Defaults to 1.

    ## Response
    * Code 200
        * **id**: Notebook id
        * **description**: Notebook description.
        * **creation_date**: Notebook creation data.
        * **modification_date**: Notebook modification data.
        * **annotations**: List of annotation id that was related.
    * Code 404
        * **detail**: Error detail.
        * **loc**: Specifies which field the error is in.
        * **msg**: Error message.
        * **type**: Error type.
    """
    return await notebook.list(response)


@router.get(
    '/{notebook_id}',
    response_model=NotebookResponse
)
async def get(
        notebook_id: str
) -> NotebookResponse:
    """
    ## Description
    * List notebook detail.

    ## Parameters
    * **notebook_id**: Id of notebook that you need to put.

    ## Response
    * Code 200
        * **id**: Notebook id
        * **description**: Notebook description.
        * **creation_date**: Notebook creation data.
        * **modification_date**: Notebook modification data.
        * **annotations**: List of annotation id that was related.
    * Code 404
        * **detail**: Error detail.
        * **loc**: Specifies which field the error is in.
        * **msg**: Error message.
        * **type**: Error type.
    """
    return await notebook.get(notebook_id)


@router.put(
    '/{notebook_id}',
    response_model=NotebookResponse
)
async def put(
        notebook_id: str,
        body: CreateAndPutNotebookRequest
) -> NotebookResponse:
    """
    ## Description
    * Update all notebook fields.

    ## Parameters
    * **notebook_id**: Id of notebook that you need to put.

    ## Body
    * **description**: Description of your annotation.
    * **annotations**: List of annotation ID that will be related.

    ## Response
    * Code 200
        * **id**: Notebook id
        * **description**: Notebook description.
        * **creation_date**: Notebook creation data.
        * **modification_date**: Notebook modification data.
        * **annotations**: List of annotation id that was related.
    * Code 404
        * **detail**: Error detail.
        * **loc**: Specifies which field the error is in.
        * **msg**: Error message.
        * **type**: Error type.
    """
    return await notebook.put(body, notebook_id)


@router.patch(
    '/{notebook_id}',
    response_model=NotebookResponse
)
async def patch(
        notebook_id: str,
        body: PatchNotebookRequest
) -> NotebookResponse:
    """
    ## Description
    * Update notebook with optional fields.

    ## Parameters
    * **notebook_id**: Id of notebook that you need to patch.

    ## Body
    * **description**: Description of your annotation.
    * **annotations**: List of annotation ID that will be related.

    ## Response
    * Code 200
        * **id**: Notebook id
        * **description**: Notebook description.
        * **creation_date**: Notebook creation data.
        * **modification_date**: Notebook modification data.
        * **annotations**: List of annotation id that was related.
    * Code 404
        * **detail**: Error detail.
        * **loc**: Specifies which field the error is in.
        * **msg**: Error message.
        * **type**: Error type.
    """
    return await notebook.patch(body, notebook_id)


@router.delete(
    '/{notebook_id}',
    status_code=status.HTTP_204_NO_CONTENT,
    response_description="No content"
)
async def delete(
        notebook_id: str
) -> Response:
    """
    ## Description
    * Delete notebook.

    ## Parameters
    * **notebook_id**: Id of annotation that you need to delete.
    """
    return await notebook.delete(notebook_id)
