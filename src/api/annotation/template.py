from datetime import datetime
from typing import List
from pydantic import BaseModel
from typing import Optional


class CreateAndPutAnnotationRequest(BaseModel):
    title: str
    tags: List[str]


class PatchAnnotationRequest(BaseModel):
    title: Optional[str] = None
    tags: Optional[List[str]] = None


class AnnotationResponse(BaseModel):
    id: str
    title: str
    creation_date: datetime
    modification_date: datetime
    tags: List[str]
