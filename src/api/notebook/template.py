import asyncio
from datetime import datetime
from typing import List
from uuid import UUID

from pydantic import BaseModel
from typing import Optional


class CreateAndPutNotebookRequest(BaseModel):
    description: str
    annotations: List[UUID]


class PatchNotebookRequest(BaseModel):
    description: Optional[str] = None
    annotations: Optional[List[UUID]] = None


class NotebookResponse(BaseModel):
    id: str
    description: str
    creation_date: datetime
    modification_date: datetime
    annotations: List[UUID]
