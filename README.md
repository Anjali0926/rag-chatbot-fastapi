# 🤖 AI-Powered RAG Chatbot

An AI-powered Retrieval-Augmented Generation (RAG) chatbot built using **FastAPI**, **LangChain**, **PostgreSQL (pgvector)**, **Hugging Face Embeddings**, **Groq LLM**, and **Streamlit**. The chatbot allows users to upload PDF documents and ask questions, returning context-aware answers using semantic search and Large Language Models (LLMs).

---

## 🚀 Features

- 📄 Upload PDF documents
- ✂️ Automatic text extraction and chunking
- 🔎 Semantic search using vector embeddings
- 🗄️ PostgreSQL with pgvector for vector storage
- 🤖 AI-powered responses using Groq LLM
- ⚡ FastAPI backend with REST APIs
- 💻 Streamlit-based user interface
- 🔒 Secure API key management using `.env`

---

# 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| Programming | Python |
| Backend | FastAPI |
| Database | PostgreSQL, pgvector |
| AI Framework | LangChain |
| Embedding Model | Hugging Face |
| LLM | Groq |
| Frontend | Streamlit |
| Environment | python-dotenv |

---

# 📂 Project Structure

```
rag-chatbot-fastapi/
│
├── AI_chatbot.py
├── chatbot.py
├── config.py
├── database.py
├── main.py
├── rag.py
├── routes.py
├── schemas.py
├── streamlit_app.py
├── vector_store.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone the repository

```bash
git clone https://github.com/Anjali0926/rag-chatbot-fastapi.git

cd rag-chatbot-fastapi
```

---

## 2️⃣ Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Configure Environment Variables

Create a `.env` file.

```env
DATABASE_URL=your_postgresql_database_url
GROQ_API_KEY=your_groq_api_key
```

---

# ▶️ Run the Backend

```bash
uvicorn main:app --reload
```

FastAPI documentation:

```
http://127.0.0.1:8000/docs
```

---

# ▶️ Run the Frontend

```bash
streamlit run streamlit_app.py
```

---

# 🔄 Application Workflow

```text
Upload PDF
      │
      ▼
Extract Text
      │
      ▼
Split into Chunks
      │
      ▼
Generate Embeddings
(Hugging Face)
      │
      ▼
Store in PostgreSQL (pgvector)
      │
      ▼
User Question
      │
      ▼
Generate Question Embedding
      │
      ▼
Semantic Similarity Search
      │
      ▼
Retrieve Relevant Chunks
      │
      ▼
Groq LLM
      │
      ▼
AI Generated Answer
```

---

# 📌 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/upload` | Upload a PDF document |
| POST | `/chat` | Ask questions about uploaded documents |

---

# 💡 Key Concepts Used

- Retrieval-Augmented Generation (RAG)
- Large Language Models (LLMs)
- Vector Embeddings
- Semantic Search
- Prompt Engineering
- FastAPI REST APIs
- PostgreSQL with pgvector
- LangChain
- Document Chunking

---

# 🔮 Future Improvements

- Support DOCX and TXT files
- Conversation memory
- Multi-document search
- Authentication and user accounts
- Docker deployment
- Cloud deployment (AWS/Azure)
- Streaming AI responses

---

# 👩‍💻 Author

**Anjali Pulusu**

- GitHub: https://github.com/Anjali0926

---

## ⭐ If you like this project, consider giving it a Star!
