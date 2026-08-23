from sqlalchemy import text
from database import SessionLocal


def add_employee(
    employee_id,
    employee_name,
    department,
    designation,
    salary
):

    db = SessionLocal()

    try:
        result = db.execute(
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
                RETURNING id
            """),
            {
                "employee_id": employee_id,
                "employee_name": employee_name,
                "department": department,
                "designation": designation,
                "salary": salary
            }
        )

        row = result.fetchone()

        db.commit()

        return row[0] if row else None

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


def get_employees():

    db = SessionLocal()

    try:
        result = db.execute(
            text("""
                SELECT
                    id,
                    employee_id,
                    employee_name,
                    department,
                    designation,
                    salary
                FROM employees
                ORDER BY id
            """)
        )

        rows = result.fetchall()

        employees = []

        for row in rows:
            employees.append({
                "id": row.id,
                "employee_id": row.employee_id,
                "employee_name": row.employee_name,
                "department": row.department,
                "designation": row.designation,
                "salary": float(row.salary)
                if row.salary is not None else 0
            })

        return employees

    finally:
        db.close()

def update_employee(
    id,
    employee_id,
    employee_name,
    department,
    designation,
    salary
):
    db = SessionLocal()

    try:
        result = db.execute(
            text("""
                UPDATE employees
                SET
                    employee_id = :employee_id,
                    employee_name = :employee_name,
                    department = :department,
                    designation = :designation,
                    salary = :salary
                WHERE id = :id
                RETURNING id
            """),
            {
                "id": id,
                "employee_id": employee_id,
                "employee_name": employee_name,
                "department": department,
                "designation": designation,
                "salary": salary
            }
        )

        row = result.fetchone()

        db.commit()

        return row[0] if row else None

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()

def delete_employee(employee_id: str):
    db = SessionLocal()

    try:
        result = db.execute(
            text("""
                DELETE FROM employees
                WHERE employee_id = :employee_id
                RETURNING employee_id
            """),
            {
                "employee_id": employee_id
            }
        )

        deleted_employee = result.fetchone()

        if not deleted_employee:
            return {
                "success": False,
                "message": f"Employee {employee_id} not found."
            }

        db.commit()

        return {
            "success": True,
            "message": f"Employee {employee_id} deleted successfully."
        }

    except Exception as e:
        db.rollback()

        return {
            "success": False,
            "message": str(e)
        }

    finally:
        db.close()

def update_employee_by_employee_id(
    employee_id,
    employee_name=None,
    department=None,
    designation=None,
    salary=None
):
    db = SessionLocal()

    try:
        updates = {}
        set_parts = []

        if employee_name is not None:
            set_parts.append("employee_name = :employee_name")
            updates["employee_name"] = employee_name

        if department is not None:
            set_parts.append("department = :department")
            updates["department"] = department

        if designation is not None:
            set_parts.append("designation = :designation")
            updates["designation"] = designation

        if salary is not None:
            set_parts.append("salary = :salary")
            updates["salary"] = salary

        if not set_parts:
            return {
                "success": False,
                "message": "No fields provided for update."
            }

        updates["employee_id"] = employee_id

        query = f"""
            UPDATE employees
            SET {", ".join(set_parts)}
            WHERE employee_id = :employee_id
            RETURNING employee_id
        """

        result = db.execute(
            text(query),
            updates
        )

        row = result.fetchone()

        if not row:
            db.rollback()

            return {
                "success": False,
                "message": f"Employee {employee_id} not found."
            }

        db.commit()

        return {
            "success": True,
            "message": f"Employee {employee_id} updated successfully."
        }

    except Exception as e:
        db.rollback()

        return {
            "success": False,
            "message": str(e)
        }

    finally:
        db.close()