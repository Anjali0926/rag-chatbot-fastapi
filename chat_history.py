from sqlalchemy import text
from database import SessionLocal


def save_message(session_id: str, role: str, message: str):

    db = SessionLocal()

    db.execute(
        text("""
            INSERT INTO chat_history
            (session_id, role, message)
            VALUES
            (:session_id, :role, :message)
        """),
        {
            "session_id": session_id,
            "role": role,
            "message": message
        }
    )

    db.commit()
    db.close()


def get_chat_history(session_id: str):

    db = SessionLocal()

    result = db.execute(
        text("""
            SELECT role, message
            FROM chat_history
            WHERE session_id = :session_id
            ORDER BY created_at
        """),
        {
            "session_id": session_id
        }
    )

    rows = result.fetchall()

    db.close()

    history = []

    for row in rows:
        history.append(
            {
                "role": row.role,
                "message": row.message
            }
        )

    return history