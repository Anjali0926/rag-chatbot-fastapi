from sqlalchemy import text

from database import SessionLocal

def save_pdf(file_name:str, pdf_data:bytes):

    db = SessionLocal()

    result = db.execute(

        text("""
          INSERT INTO pdf_documents
          (file_name, pdf_data)
          VALUES
          (:file_name, :pdf_data)
          RETURNING id

    """),

    {
        "file_name": file_name,
        "pdf_data": pdf_data
    }

    )

    document_id = result.scalar()

    db.commit()

    db.close()

    return document_id

def get_pdf(document_id: int):

    db = SessionLocal()

    result = db.execute(
        text("""
            SELECT file_name, pdf_data
            FROM pdf_documents
            WHERE id = :id
        """),
        {
            "id": document_id
        }
    )

    row = result.fetchone()

    db.close()

    return row

import tempfile

def create_temp_pdf(file_name: str):

    row = get_pdf_by_filename(file_name)

    if row is None:
        return None

    temp_file = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    )

    temp_file.write(bytes(row.pdf_data))
    temp_file.close()

    return temp_file.name

from sqlalchemy import text
from database import SessionLocal


def get_all_documents():

    db = SessionLocal()

    result = db.execute(
        text("""
            SELECT id, file_name
            FROM pdf_documents
            ORDER BY id

        """)
    )

    rows = result.fetchall()

    db.close()

    return rows

def get_pdf_by_filename(file_name: str):

    db = SessionLocal()

    result = db.execute(
        text("""
            SELECT id, file_name, pdf_data
            FROM pdf_documents
            WHERE file_name = :file_name
        """),
        {
            "file_name": file_name
        }
    )

    row = result.fetchone()

    db.close()

    return row