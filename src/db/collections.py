from datetime import datetime
from typing import List
from uuid import UUID, uuid4

from beanie import Document
from pydantic import Field


class AnnotationDocument(Document):
    id: UUID = Field(default_factory=uuid4)
    title: str
    creation_date: datetime
    modification_date: datetime
    tags: List[str]

    class Collection:
        name = "AnnotationDescription"


class NotebookDocument(Document):
    id: UUID = Field(default_factory=uuid4)
    description: str
    creation_date: datetime
    modification_date: datetime
    annotations: List[UUID]

    class Collection:
        name = "NotebookDescription"
