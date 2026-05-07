from fastapi import FastAPI,File,UploadFile
import pandas as pd
from PyPDF2 import PdfReader
import io


app=FastAPI()

@app.post("/read-file/")

async def read_file(file:UploadFile=File(...)):
    content= await file.read()
    name=file.filename.lower()

    if name.endswith((".xl",".xlsx")):
        xlreader=pd.read_excel(io.BytesIO(content))
        xlreader = xlreader.fillna("")
        return {
            "Type":"Excel",
            "preview":xlreader.head(10).to_dict(orient="records")
        }


    elif name.endswith(".pdf"):
        pdfreader=PdfReader(io.BytesIO(content))
        text="".join([p.extract_text() or "" for p in pdfreader.pages[:2]])
        return {
            "Type":"PDF",
            "preview":text.strip()[:500]
        }

    return {"Error":"unsupported file format"}
