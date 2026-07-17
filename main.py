from fastapi import FastAPI

from routes import router

app = FastAPI(
   title = "RAG Chatbot API",
   description = "RAG Chatbot using FastAPI, Langchain, PGVector and Groq",
   version="1.0.0"
)

app.include_router(router)

@app.get("/")
def home():
    return{
      "message": "RAG Chatbot API is running"
    }