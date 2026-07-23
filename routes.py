from fastapi import APIRouter, UploadFile, File, HTTPException
import os

from chat_history import save_message

from documents import save_pdf, create_temp_pdf

from rag import rag_pdf

from chatbot import ask_question

from schemas import ChatRequest, ChatResponse

router = APIRouter()

#upload API

@router.post("/upload")
def upload_pdf(file: UploadFile = File(...)):

    pdf_bytes = file.file.read()

    document_id = save_pdf(
        file.filename,
        pdf_bytes
    )
    
    temp_pdf = create_temp_pdf(document_id)

    try:
          rag_pdf(temp_pdf)

    finally:
             if temp_pdf and os.path.exists(temp_pdf):
                os.remove(temp_pdf)

    return {
        "message": "PDF uploaded successfully.",
        "document_id": document_id,
        "file_name": file.filename
    }


@router.post("/index/{file_name}")
def reindex(file_name: str):

    temp_pdf = create_temp_pdf(file_name)

    if temp_pdf is None:
        raise HTTPException(
            status_code=404,
            detail="Document not found."
        )

    try:
        rag_pdf(temp_pdf)

    finally:
             if temp_pdf and os.path.exists(temp_pdf):
               os.remove(temp_pdf)

    return {
        "message": "Document indexed successfully."
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
