from langchain_groq import ChatGroq

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from chat_history import get_chat_history

from config import GROQ_API_KEY

from vector_store import vector_store

from agents.agent import agent

import re



# STEP 1 - RETRIEVER


retriever = vector_store.as_retriever(
    search_kwargs={"k": 10}
)



# STEP 2 - LLM


llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model="qwen/qwen3.6-27b",
    temperature=0,
    reasoning_effort="none",
    reasoning_format="hidden"
)



# RAG PROMPT


prompt = ChatPromptTemplate.from_template("""
You are a helpful AI assistant.

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



# OUTPUT PARSER


parser = StrOutputParser()



# FORMAT DOCUMENTS


def format_docs(docs):
    return "\n\n".join(
        doc.page_content
        for doc in docs
    )



# RAG CHAIN


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



# ASK QUESTION


def ask_question(question: str, session_id: str):

    
    # GREETINGS
    

    greetings = {
        "hi": "Hello! How can I help you today?",
        "hello": "Hello! How can I help you today?",
        "hey": "Hi! How can I assist you?",
        "good morning": "Good morning! How can I help you?",
        "good afternoon": "Good afternoon! How can I help you?",
        "good evening": "Good evening! How can I assist you?"
    }

    user_question = question.lower().strip()

    if user_question in greetings:
        return greetings[user_question]


   
    # GET PREVIOUS CONVERSATION
   

    history = get_chat_history(session_id)

    history_text = ""

    for chat in history:

        if chat["role"] == "user":

            history_text += (
                f"User: {chat['message']}\n"
            )

        else:

            history_text += (
                f"Assistant: {chat['message']}\n"
            )

    # EMPLOYEE CRUD DETECTION

    crud_keywords = [
        "add",
        "create",
        "update",
        "edit",
        "change",
        "delete",
        "remove",
        "show",
        "list",
        "get",
        "view"
    ]


    # Check for CRUD keyword

    has_crud_request = any(
        re.search(
            rf"\b{keyword}\b",
            user_question
        )
        for keyword in crud_keywords
    )


    # Check for employee ID
    # Examples: EMP01, EMP012, EMP100

    has_employee_id = re.search(
        r"\bEMP\d+\b",
        user_question,
        re.IGNORECASE
    )


    # Check if "employee" or "employees" exists

    has_employee_word = (
        "employee" in user_question
        or "employees" in user_question
    )


  
    # FINAL CRUD DECISION
   
    is_crud_request = (
        has_crud_request
        and (
            has_employee_id is not None
            or has_employee_word
        )
    )
  
    # DEBUG

    print("\n========================================")
    print("QUESTION:", question)
    print("CRUD REQUEST:", has_crud_request)
    print("EMPLOYEE ID:", has_employee_id)
    print("EMPLOYEE WORD:", has_employee_word)
    print("IS CRUD REQUEST:", is_crud_request)
    print("========================================")

    # CRUD → LANGGRAPH AGENT
   
    if is_crud_request:

        result = agent.invoke({
            "messages": [
                {
                    "role": "user",
                    "content": question
                }
            ]
        })


        print("\n========== AGENT RESULT ==========")
        print(result)


        final_message = result["messages"][-1]


        print("\n========== FINAL MESSAGE ==========")
        print(final_message)


        return final_message.content
   
    # NORMAL QUESTION → EXISTING RAG

    return chain.invoke({
        "question": question,
        "history": history_text
    })