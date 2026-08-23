import os

from documents import get_all_documents, create_temp_pdf
from rag import rag_pdf


def index_all_documents():

    documents = get_all_documents()

    for document in documents:


        print(document)
        print(document.file_name)
        temp_pdf = create_temp_pdf(document.file_name)

        if temp_pdf is None:
            continue

        try:
            rag_pdf(temp_pdf)

        finally:
            if os.path.exists(temp_pdf):
                os.remove(temp_pdf)

    print("All documents indexed successfully.")