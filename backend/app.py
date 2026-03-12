from fastapi import FastAPI, UploadFile, File, Query
from typing import List
import os

from backend.rag_chain import create_rag_chain
from backend.database import save_chat

app = FastAPI()

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

qa_chain = None


@app.get("/")
def home():
    return {"message": "RAG API Running"}


# Upload PDFs
@app.post("/upload")
async def upload_pdfs(files: List[UploadFile] = File(...)):

    global qa_chain

    paths = []

    for file in files:

        file_path = os.path.join(UPLOAD_FOLDER, file.filename)

        with open(file_path, "wb") as f:
            f.write(await file.read())

        paths.append(file_path)

    qa_chain = create_rag_chain(paths)

    return {"message": "PDFs uploaded and RAG initialized"}


# Ask question
@app.get("/ask")
async def ask_question(question: str = Query(...)):

    global qa_chain

    if qa_chain is None:
        return {"answer": "Please upload PDFs first"}

    result = qa_chain.invoke({"query": question})

    answer = result["result"]

    save_chat(question, answer)

    return {"answer": answer}