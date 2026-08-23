import pandas as pd
from sqlalchemy import text
from database import SessionLocal

def upload_employee_excel(file_path: str):
    df = pd.read_excel(file_path)
    db = SessionLocal()

    try:
        for  _, row in df.iterrows():

            db.execute(
                text(""" 
                       INSERT INTO employees
                       (
                          employee_id,
                          employee_name,
                          department,
                          designation,
                          salary
                        )
                        VALUES
                        (
                          :employee_id,
                          :employee_name,
                          :department,
                          :designation,
                          :salary
                        )
                """),
                {
                    "employee_id": row["Employee ID"],
                    "employee_name": row["Employee Name"],
                    "department": row["Department"],
                    "designation": row["Designation"],
                    "salary": row["Salary"],
                }
            )

            db.commit()

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()