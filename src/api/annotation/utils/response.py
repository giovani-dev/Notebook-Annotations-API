from src.api.annotation.template import AnnotationResponse


async def annotation_response(document):
    return AnnotationResponse(
        id=str(document.id),
        title=document.title,
        creation_date=document.creation_date,
        modification_date=document.modification_date,
        tags=document.tags,
    )