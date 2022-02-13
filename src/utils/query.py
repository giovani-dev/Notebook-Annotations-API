from uuid import UUID

from beanie import Document

from src.utils.http_exception import not_found


async def get_document_with_id(
        _id: str,
        document_class: Document,
        error_message: str
) -> Document:
    if isinstance(_id, str):
        _id = UUID(_id)
    document = await document_class.find_one(
        document_class.id == _id
    )
    await not_found(data=document, error_message=error_message)
    return document

