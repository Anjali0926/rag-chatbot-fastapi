import streamlit as st
import requests

st.set_page_config(
    page_title="RAG Chatbot",
    page_icon="🤖"
)

st.title("🤖 RAG Chatbot")

st.write("Upload a PDF and ask questions about it.")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file is not None:

    if st.button("Upload PDF"):

        files = {
            "file": (
                uploaded_file.name,
                uploaded_file,
                "application/pdf"
            )
        }

        response = requests.post(
            "http://127.0.0.1:8000/upload",
            files=files
        )

        if response.status_code == 200:
            st.success("PDF Uploaded Successfully!")

        else:
            st.error("Upload Failed")


question = st.text_input(
    "Ask a Question"
)

if st.button("Ask"):

    response = requests.post(
        "http://127.0.0.1:8000/chat",
        json={
            "session_id": "user1",
            "question": question
        }
    )

    if response.status_code == 200:

        answer = response.json()["answer"]

        st.success(answer)

    else:
        st.error("Something went wrong.")