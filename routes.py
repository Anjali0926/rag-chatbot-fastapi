from fastapi import APIRouter, UploadFile, File

import os

import shutil #used to save the uploaded file

from rag import rag_pdf

from chatbot import ask_question

from schemas import ChatRequest, ChatResponse

router = APIRouter()

#upload API

@router.post("/upload")
def upload_pdf(file: UploadFile = File(...)):

    os.makedirs("uploads", exist_ok=True)

    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    rag_pdf(file_path)

    return {
        "message": "PDF uploaded successfully."
    }


@router.post(
    "/chat",
    response_model=ChatResponse
)
def chat(request: ChatRequest):

    answer = ask_question(request.question)

    return ChatResponse(
        answer=answer
    )

