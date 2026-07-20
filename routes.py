from fastapi import APIRouter, UploadFile, File

from chat_history import save_message

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

    #saving the user question

    save_message(
        request.session_id,
        "user",
        request.question
    )

    #ask chatbot
    answer = ask_question(
        question=request.question,
        session_id=request.session_id
        )

    #2save the assistant answer
    save_message(
        request.session_id,
        "assistant",
        answer
    )

    return ChatResponse(
        answer=answer
    )

