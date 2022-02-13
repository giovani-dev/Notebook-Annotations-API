from src.api.notebook.template import NotebookResponse


async def notebook_response(document):
    return NotebookResponse(
        id=str(document.id),
        description=document.description,
        creation_date=document.creation_date,
        modification_date=document.modification_date,
        annotations=document.annotations,
    )