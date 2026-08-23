from langchain_huggingface import HuggingFaceEmbeddings

from langchain_postgres import PGVector

from config import DATABASE_URL

embedding_mmodel = HuggingFaceEmbeddings(
    model="BAAI/bge-small-en-v1.5"
)

vector_store = PGVector(
    embeddings = embedding_mmodel,
    collection_name="documents",
    connection=DATABASE_URL,
)
