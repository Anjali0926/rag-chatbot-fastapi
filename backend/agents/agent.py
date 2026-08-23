from typing import Annotated, TypedDict

from langchain_groq import ChatGroq
from langchain_core.tools import tool

from langgraph.graph import StateGraph, START
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.graph.message import add_messages

from config import GROQ_API_KEY

from agents.tools import employee_tools

from vector_store import vector_store

# RAG RETRIEVER

retriever = vector_store.as_retriever(
    search_kwargs={"k": 10}
)

# LLM

llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model="qwen/qwen3.6-27b",
    temperature=0,
    reasoning_effort="none",
    reasoning_format="hidden"
)

# RAG TOOL

@tool
def search_documents(question: str) -> str:
    """
    Search uploaded PDF documents.

    Use this ONLY for questions about PDF documents,
    policies, company information, or uploaded documents.

    Do NOT use this tool for employee CRUD operations.
    """

    docs = retriever.invoke(question)

    if not docs:
        return "I don't know"

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    return context

# ALL TOOLS

tools = [
    search_documents,
    *employee_tools
]
# AGENT STATE

class AgentState(TypedDict):
    messages: Annotated[list, add_messages]

# LLM WITH TOOLS

llm_with_tools = llm.bind_tools(tools)

# CHATBOT

def chatbot(state: AgentState):

    system_message = {
        "role": "system",
        "content": """
You are an employee management AI assistant.

You have the following employee CRUD tools:

1. create_employee_tool
2. get_employees_tool
3. update_employee_tool
4. delete_employee_tool

You also have:

5. search_documents


==================================================
EMPLOYEE CRUD RULES
==================================================

CREATE:

If the user asks to:

- create an employee
- add an employee
- insert an employee

MUST call:

create_employee_tool


==================================================
READ / LIST
==================================================

If the user asks to:

- show employees
- list employees
- get employees
- view employees
- display employees

MUST call:

get_employees_tool


==================================================
UPDATE
==================================================

If the user asks to:

- update an employee
- edit an employee
- change employee details
- modify employee details

MUST call:

update_employee_tool


IMPORTANT:

If the user says:

"update EMP01 salary 95000"

you MUST call:

update_employee_tool

with:

employee_id = "EMP01"
salary = 95000

DO NOT call get_employees_tool.

DO NOT call search_documents.

Updating an employee is NOT the same as listing employees.


==================================================
DELETE
==================================================

If the user asks to:

- delete an employee
- remove an employee

MUST call:

delete_employee_tool


==================================================
DOCUMENT QUESTIONS
==================================================

Use search_documents ONLY when the user asks about:

- uploaded PDFs
- company policies
- document information
- information contained in uploaded documents

Do NOT use search_documents for employee CRUD.


==================================================
IMPORTANT
==================================================

Never invent employee data.

Always use the appropriate employee tool for CRUD requests.

After a successful CRUD operation, return the result
from the tool as a short confirmation.

If an employee does not exist, clearly tell the user.
"""
    }


    # =====================================================
    # CALL LLM
    # =====================================================

    response = llm_with_tools.invoke(
        [system_message] + state["messages"]
    )


    # =====================================================
    # DEBUG TOOL CALL
    # =====================================================

    print("\n========================================")
    print("LLM RESPONSE")
    print(response)

    print("\nTOOL CALLS:")
    print(response.tool_calls)

    print("========================================\n")


    return {
        "messages": [response]
    }

# TOOL NODE

tool_node = ToolNode(tools)

# GRAPH

graph = StateGraph(AgentState)

graph.add_node(
    "chatbot",
    chatbot
)

graph.add_node(
    "tools",
    tool_node
)

# EDGES

graph.add_edge(
    START,
    "chatbot"
)

graph.add_conditional_edges(
    "chatbot",
    tools_condition
)

graph.add_edge(
    "tools",
    "chatbot"
)

# COMPILE

agent = graph.compile()