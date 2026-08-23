from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
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



app.add_middleware(
    CORSMiddleware,

    allow_origins="http://localhost:5173", 
        #list of allowed origins
    allow_credentials=True,  
                                        #like cookies or authorization headers are permitted
    allow_methods=["*"],  
                #(a "wildcard") http methods allowed for cross-origin requests (get,post)
    allow_headers=["*"],         #http headers allowed in requeste
)


