from fastapi import FastAPI

from routes import router
from startup import index_all_documents

app = FastAPI(
   title = "RAG Chatbot API",
   description = "RAG Chatbot using FastAPI, Langchain, PGVector and Groq",
   version="1.0.0"
)

@app.on_event("startup")
def startup_event():
    index_all_documents()

app.include_router(router)

@app.get("/")
def home():
    return{
      "message": "RAG Chatbot API is running"
    }



