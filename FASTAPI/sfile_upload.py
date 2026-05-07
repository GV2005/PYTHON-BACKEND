from fastapi import FastAPI,File,UploadFile

app=FastAPI()

@app.post("/fileupload/")

async def file_upload(file:UploadFile = File(...)):
    content=await file.read()

    try:
        text_p=content.decode("utf-8")[:200]

    except:
        text_p="content cannot be displayed as text"


    return {
        "file name":file.filename,
        "file type":file.content_type,
        "size":len(content),
        "Text":text_p
    }