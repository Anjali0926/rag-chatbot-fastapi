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

def get_all_sessions():
    db = SessionLocal()

    result = db.execute(
        text("""
              SELECT 
                 session_id,
                 MIN(message) AS title,
                 MAX(created_at) AS last_message
              FROM chat_history
              WHERE role = 'user'
              GROUP BY session_id
              ORDER BY last_message DESC;
        """)
    )

    rows = result.fetchall()

    db.close()

    sessions = []

    for row in rows:
        sessions.append({
            "session_id": row.session_id,
            "title": row.title
     })

    return sessions