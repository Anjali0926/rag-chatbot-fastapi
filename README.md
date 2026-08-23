
# 🤖 AI-Powered RAG Chatbot with Employee Management

An AI-powered **Retrieval-Augmented Generation (RAG) chatbot** built using **FastAPI, React, Tailwind CSS, PostgreSQL, pgvector, LangChain, Hugging Face Embeddings, and Groq**.

The chatbot is designed to answer questions based on an **Employee Handbook** and also perform **employee CRUD operations through a chatbot interface**.

---

## Features

### RAG Chatbot

* Upload and process PDF documents
* Extract text from PDF documents
* Split documents into smaller chunks
* Generate vector embeddings
* Store embeddings in PostgreSQL using pgvector
* Perform semantic similarity search
* Retrieve relevant document content
* Generate context-aware answers using Groq LLM

###  Employee Management

The chatbot can perform employee-related operations through natural language:

* Create employee records
* Retrieve employee information
* Update employee information
* Delete employee records
* Query employee data through the chatbot

###  Chatbot Interface

* Interactive chatbot widget
* Chat history
* Session-based conversations
* Employee queries through natural language
* Employee handbook question answering

###  Frontend

* React
* Tailwind CSS
* Vite
* Responsive UI
* Chatbot widget
* PDF upload interface
* Employee management interface

---

#  Tech Stack

| Category              | Technologies           |
| --------------------- | ---------------------- |
| Programming Language  | Python, JavaScript     |
| Backend               | FastAPI                |
| Frontend              | React                  |
| Styling               | Tailwind CSS           |
| Build Tool            | Vite                   |
| Database              | PostgreSQL             |
| Vector Database       | pgvector               |
| AI Framework          | LangChain              |
| Embeddings            | Hugging Face           |
| Embedding Model       | BAAI/bge-small-en-v1.5 |
| LLM                   | Groq                   |
| LLM Model             | Qwen 3.6 27B           |
| PDF Processing        | PyPDF                  |
| ORM / Database Access | SQLAlchemy             |
| Environment Variables | python-dotenv          |

---

#  Project Structure

```text
RAG_project/
│
├── backend/
│   │
│   ├── agents/
│   │   ├── agent.py
│   │   └── tools.py
│   │
│   ├── main.py
│   ├── database.py
│   ├── documents.py
│   ├── rag.py
│   ├── vector_store.py
│   ├── chatbot.py
│   ├── chat_history.py
│   ├── employee.py
│   ├── excel_upload.py
│   ├── routes.py
│   ├── schemas.py
│   ├── config.py
│   ├── startup.py
│   ├── test_agent.py
│   ├── requirements.txt
│   └── uploads/
│
├── frontend/
│   │
│   ├── public/
│   │
│   ├── src/
│   │   ├── components/
│   │   │   ├── ChatBot.jsx
│   │   │   ├── ChatInput.jsx
│   │   │   ├── ChatMessage.jsx
│   │   │   ├── ChatWidget.jsx
│   │   │   ├── Features.jsx
│   │   │   ├── Footer.jsx
│   │   │   ├── Header.jsx
│   │   │   ├── Hero.jsx
│   │   │   ├── Sidebar.jsx
│   │   │   └── UploadPDF.jsx
│   │   │
│   │   ├── pages/
│   │   │   ├── EmployeeManagement.jsx
│   │   │   └── Home.jsx
│   │   │
│   │   ├── App.jsx
│   │   ├── App.css
│   │   ├── index.css
│   │   └── main.jsx
│   │
│   ├── package.json
│   ├── package-lock.json
│   └── vite.config.js
│
├── .gitignore
└── README.md
```

---

#  Installation

## 1. Clone the Repository

```bash
git clone https://github.com/Anjali0926/rag_chatbot.git

cd rag_chatbot
```

---

#  Backend Setup

## 2. Create a Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## 3. Install Backend Dependencies

Navigate to the backend folder:

```bash
cd backend
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

#  Environment Variables

Create a `.env` file in the backend directory.

```env
DATABASE_URL=your_postgresql_database_url
GROQ_API_KEY=your_groq_api_key
MODEL_NAME=qwen/qwen3.6-27b
```

Do **not** commit the `.env` file to GitHub.

---

#  PostgreSQL and pgvector

The project uses PostgreSQL with the **pgvector extension** for storing and searching vector embeddings.

The RAG pipeline stores:

* Document chunks
* Vector embeddings
* Document metadata

The original PDF files can also be stored in PostgreSQL through the `pdf_documents` table.

---

#  Run the Backend

From the `backend` directory:

```bash
uvicorn main:app --reload
```

The FastAPI backend will run at:

```text
http://127.0.0.1:8000
```

FastAPI Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

---

#  Frontend Setup

Open another terminal and navigate to the frontend:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the React development server:

```bash
npm run dev
```

The frontend will normally be available at:

```text
http://localhost:5173
```

---

#  RAG Application Workflow

```text
                PDF Document
                     │
                     ▼
                Upload PDF
                     │
                     ▼
              Extract PDF Text
                     │
                     ▼
             Split into Chunks
                     │
                     ▼
          Generate Embeddings
          (Hugging Face Model)
                     │
                     ▼
          Store in PostgreSQL
                + pgvector
                     │
                     │
        ─────────────┴─────────────
                     │
               User Question
                     │
                     ▼
          Generate Question
              Embedding
                     │
                     ▼
          Similarity Search
              in pgvector
                     │
                     ▼
          Retrieve Relevant
               Chunks
                     │
                     ▼
              Qwen LLM
               via Groq
                     │
                     ▼
             Final Answer
```

---

#  Employee Chatbot Workflow

The chatbot can also interact with employee data using natural language.

```text
User
 │
 ▼
Chatbot Widget
 │
 ▼
Understand User Request
 │
 ├── Employee Handbook Question
 │          │
 │          ▼
 │       RAG Search
 │          │
 │          ▼
 │       Qwen LLM
 │
 └── Employee Operation
            │
            ▼
        CRUD Tool
            │
            ├── Create Employee
            ├── Get Employee
            ├── Update Employee
            └── Delete Employee
            │
            ▼
        PostgreSQL
            │
            ▼
        Chatbot Response
```

---

#  API Endpoints

The FastAPI backend provides endpoints for document processing, chatbot interaction, employee management, and conversation handling.

| Method | Endpoint                | Purpose                            |
| ------ | ----------------------- | ---------------------------------- |
| POST   | `/upload`               | Upload and process a PDF           |
| POST   | `/chat`                 | Ask a question through the chatbot |
| GET    | `/history/{session_id}` | Retrieve conversation history      |
| GET    | `/sessions`             | Retrieve available chat sessions   |
| GET    | `/employees`            | Retrieve employee records          |
| POST   | Employee CRUD endpoints | Manage employee records            |

> The exact employee endpoint names can be viewed through the FastAPI Swagger documentation at `/docs`.

---

#  AI and RAG Concepts Used

This project demonstrates several concepts in Generative AI and RAG:

* Retrieval-Augmented Generation
* Large Language Models
* Vector Embeddings
* Semantic Search
* Document Chunking
* Prompt Engineering
* Vector Databases
* LangChain
* Tool Calling
* AI Agents
* Conversation Memory
* PostgreSQL
* pgvector

---

# 📄 Document Processing

The application processes PDF documents through the following pipeline:

```text
PDF
 ↓
PyPDFLoader
 ↓
Text Extraction
 ↓
RecursiveCharacterTextSplitter
 ↓
Document Chunks
 ↓
Hugging Face Embeddings
 ↓
PostgreSQL + pgvector
```

Once a document has been indexed, its embeddings can be reused for future chatbot queries without regenerating them every time the application starts.

---

#  Employee CRUD Through Chatbot

Instead of manually performing every employee operation through a traditional form, the chatbot can understand natural-language requests.

For example:

```text
Create an employee named Rahul with employee ID EMP101.
```

or:

```text
Show me the employee with ID EMP101.
```

or:

```text
Update Rahul's department to IT.
```

or:

```text
Delete employee EMP101.
```

The chatbot uses backend tools to perform the corresponding database operation.

---

#  Security

Sensitive configuration values are stored in environment variables.

Example:

```env
GROQ_API_KEY=your_api_key
DATABASE_URL=your_database_url
```

The `.env` file is excluded from Git using `.gitignore`.

Never expose API keys or database credentials in source code.

---

#  Future Improvements

* Multi-document management
* DOCX and TXT document support
* Authentication and authorization
* Improved conversation memory
* Streaming AI responses
* Advanced multi-agent workflows
* Docker deployment
* Cloud deployment
* Production database configuration
* Better document source citations
* Role-based employee access

---

#  Author

**Anjali Pulusu**

GitHub:
[https://github.com/Anjali0926](https://github.com/Anjali0926)

---

##  Project

If you find this project useful, consider giving the repository a ⭐ on GitHub.
