from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

def chat_groq(prompt):
    response = llm.invoke(prompt)
    return response.content

while True:
    
    user_input = input("You: ")

    if user_input.lower() == "bye":
        print("Chatbot: bye")
        break

    response = chat_groq(user_input)
    print("Chatbot: ", response)

