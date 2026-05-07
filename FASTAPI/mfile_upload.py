from fastapi import FastAPI, UploadFile, File
from typing import Annotated

app = FastAPI(openapi_version="3.0.3")

@app.post("/multifileupload/")
async def file_upload(
    files: Annotated[list[UploadFile], File(...)]
):
    result = []

    for file in files:
        content = await file.read()

        try:
            text_p = content.decode("utf-8")[:200]
        except UnicodeDecodeError:
            text_p = "content cannot be displayed as text"

        result.append({
            "file_name": file.filename,
            "file_type": file.content_type,
            "size": len(content),
            "text": text_p
        })

    return result