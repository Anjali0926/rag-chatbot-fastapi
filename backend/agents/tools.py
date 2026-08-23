from langchain_core.tools import tool

from employee import (
    add_employee,
    get_employees,
    update_employee_by_employee_id,
    delete_employee
)


@tool
def create_employee_tool(
    employee_id: str,
    employee_name: str,
    department: str,
    designation: str,
    salary: float
):
    """
    Create a new employee in the database.
    """

    try:
        employee_db_id = add_employee(
            employee_id,
            employee_name,
            department,
            designation,
            salary
        )

        return {
            "success": True,
            "message": f"Employee {employee_id} added successfully.",
            "id": employee_db_id
        }

    except Exception as e:
        return {
            "success": False,
            "message": str(e)
        }


@tool
def get_employees_tool():
    """
    Get/list/show all employees.

    Use this tool ONLY when the user asks to
    view, show, list, get, or display employees.

    Do NOT use this tool for update requests.
    """

    try:
        employees = get_employees()

        return {
            "success": True,
            "employees": employees
        }

    except Exception as e:
        return {
            "success": False,
            "message": str(e)
        }

@tool
def update_employee_tool(
    employee_id: str,
    employee_name: str = None,
    department: str = None,
    designation: str = None,
    salary: float = None
):
    """
    Update an existing employee.

    Use this tool ONLY when the user wants to
    update, edit, modify, or change employee data.

    Example:

    update EMP01 salary 95000

    This means:

    employee_id = EMP01
    salary = 95000

    Only the fields provided by the user should be updated.
    """

    try:
        return update_employee_by_employee_id(
            employee_id=employee_id,
            employee_name=employee_name,
            department=department,
            designation=designation,
            salary=salary
        )

    except Exception as e:
        return {
            "success": False,
            "message": str(e)
        }

@tool
def delete_employee_tool(employee_id: str):
    """
    Delete an employee using employee ID such as EMP014.
    Use this tool when the user asks to delete or remove an employee.
    """

    try:
        return delete_employee(employee_id)

    except Exception as e:
        return {
            "success": False,
            "message": str(e)
        }


employee_tools = [
    create_employee_tool,
    get_employees_tool,
    update_employee_tool,
    delete_employee_tool
]