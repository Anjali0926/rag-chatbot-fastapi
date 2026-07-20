from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from vector_store import vector_store


def rag_pdf(pdf_path: str):

    loader = PyPDFLoader(pdf_path)

    documents = loader.load()

    print("=" * 50)
    print("DOCUMENTS LOADED")
    print("=" * 50)

    print(f"Pages: {len(documents)}")

    for i, doc in enumerate(documents):
        print(f"\nPage {i+1}")
        print(doc.page_content)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(documents)

    try:
      vector_store.delete_collection()
    except:
      pass

    vector_store.create_collection()

    vector_store.add_documents(chunks)

    print("PDF Indexed Successfully!")
