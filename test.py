# from chat_history import get_chat_history

# history = get_chat_history("user1")

# print(history)

from documents import get_pdf

row = get_pdf(1)

print(row.file_name)
print(type(row.pdf_data))

from documents import create_temp_pdf

pdf_path = create_temp_pdf(1)

print(pdf_path)

from documents import create_temp_pdf
from rag import rag_pdf

pdf_path = create_temp_pdf(1)

rag_pdf(pdf_path)