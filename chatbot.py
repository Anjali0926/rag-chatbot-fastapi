from langchain_groq import ChatGroq

from langchain_core.prompts import ChatPromptTemplate

from langchain_core.output_parsers import StrOutputParser

from langchain_core.runnables import RunnablePassthrough

from chat_history import get_chat_history

from config import GROQ_API_KEY

from vector_store import vector_store

#step1--- retriever

retriever = vector_store.as_retriever(
    search_kwargs={"k":10}
)

#step2--- LLm

llm = ChatGroq(
    groq_api_key = GROQ_API_KEY,
    model = "llama-3.3-70b-versatile",
    temperature=0
)

prompt = ChatPromptTemplate.from_template("""
    You are a helpful AI assistant
    Answer only using the provided content.
                                                                                  
    If the answer is not found in the context, reply exactly:

    "I don't know"
   
   Previous Conversation:
   {history}
                                          
    Context:
    {context} 
    Question:                                       
    {question}
                                                     
    Answer:                                   
""")

parser = StrOutputParser()

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

chain = (
    {
        "context": (
            lambda x: x["question"]
        )
        | retriever
        | format_docs,

        "question": lambda x: x["question"],

        "history": lambda x: x["history"],
    }
    | prompt
    | llm
    | parser
)

def ask_question(question: str, session_id:str): #reusable function
    history = get_chat_history(session_id)

    history_text = ""

    for chat in history:

        if chat["role"] == "user":
            history_text += f"User: {chat['message']}\n"

        else:
            history_text += f"Assistant: {chat['message']}\n"

    return chain.invoke(
        {
            "question": question,
            "history": history_text
        }
    )

