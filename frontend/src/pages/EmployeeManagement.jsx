import { useEffect, useState } from "react";

function EmployeeManagement() {

    const [employees, setEmployees] = useState([]);
    const [loading, setLoading] = useState(true);

    // GET EMPLOYEES
   
    const loadEmployees = async () => {

        try {

            const response = await fetch(
                "http://127.0.0.1:8000/employees"
            );

            if (!response.ok) {
                throw new Error("Failed to load employees");
            }

            const data = await response.json();

            setEmployees(data.employees);

        } catch (error) {

            console.error(
                "Error loading employees:",
                error
            );

        } finally {

            setLoading(false);

        }
    };

    // LOAD EMPLOYEES WHEN PAGE OPENS

    useEffect(() => {

        loadEmployees();

    }, []);

    // LOADING

    if (loading) {

        return (
            <div className="min-h-screen bg-gray-100 p-8">

                <p className="text-gray-600">
                    Loading employees...
                </p>

            </div>
        );
    }


    // UI

    return (

        <div className="min-h-screen bg-gray-100 p-8">

            {/* Page Heading */}

            <h1 className="text-3xl font-bold text-gray-800 mb-6">
                Employee Management
            </h1>


            {/* Employee Table */}

            <div className="bg-white rounded-xl shadow overflow-hidden">

                <div className="overflow-x-auto">

                    <table className="w-full">

                        {/* Table Header */}

                        <thead className="bg-gray-800 text-white">

                            <tr>

                                <th className="px-6 py-3 text-left">
                                    Employee ID
                                </th>

                                <th className="px-6 py-3 text-left">
                                    Name
                                </th>

                                <th className="px-6 py-3 text-left">
                                    Department
                                </th>

                                <th className="px-6 py-3 text-left">
                                    Designation
                                </th>

                                <th className="px-6 py-3 text-left">
                                    Salary
                                </th>

                            </tr>

                        </thead>


                        {/* Table Body */}

                        <tbody>

                            {employees.map((employee) => (

                                <tr
                                    key={employee.id}
                                    className="border-b hover:bg-gray-50"
                                >

                                    {/* Employee ID */}

                                    <td className="px-6 py-4 font-medium">
                                        {employee.employee_id}
                                    </td>


                                    {/* Name */}

                                    <td className="px-6 py-4">
                                        {employee.employee_name}
                                    </td>


                                    {/* Department */}

                                    <td className="px-6 py-4">
                                        {employee.department}
                                    </td>


                                    {/* Designation */}

                                    <td className="px-6 py-4">
                                        {employee.designation}
                                    </td>


                                    {/* Salary */}

                                    <td className="px-6 py-4">
                                        ₹{employee.salary}
                                    </td>

                                </tr>

                            ))}

                        </tbody>

                    </table>

                </div>

            </div>

        </div>
    );
}

export default EmployeeManagement;