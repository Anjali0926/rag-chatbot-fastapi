from langchain_groq import ChatGroq

from langchain_core.prompts import ChatPromptTemplate

from langchain_core.output_parsers import StrOutputParser

from langchain_core.runnables import RunnablePassthrough

from config import GROQ_API_KEY

from vector_store import vector_store

#step1--- retriever

retriever = vector_store.as_retriever(
    search_kwargs={"k":3}
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

                                          
    Context:
         {context} 
    Question:                                       {question}
                                                     
    Answer:                                   
""")

parser = StrOutputParser()

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

chain = (
   {
     "context": retriever | format_docs,
    "question": RunnablePassthrough(),
   }
   |prompt
   |llm
   |parser
)

def ask_question(question: str): #reusable function
    return chain.invoke(question)

if __name__ == "__main__":
    question = "What is FastAPI?"
    answer = ask_question(question)

    print("\nQuestion: ")
    print(question)

    print("\nAnswer: ")
    print(answer)


