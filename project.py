import pyodbc


# Establish connection to SQL Server
def conection():
    driver = "SQL SERVER"
    server = "DESKTOP-ED704T0\\MOHAMED"
    db = "EmployeeDB"

    conString = f'DRIVER={driver};SERVER={server};DATABASE={db};Trusted_Connection=yes'
    con = pyodbc.connect(conString)
    return con


def add_employee():
    # Function to add a new employee
    conn = conection()
    cursor = conn.cursor()
    id = int(input("Enter employee ID: "))
    name = input("Enter employee name: ")
    age = int(input("Enter employee age: "))
    position = input("Enter employee position: ")
    salary = float(input("Enter employee salary: "))
    cursor.execute("INSERT INTO Employees (id, name, age, position, salary) VALUES (?, ?, ?, ?, ?)",
                   (id, name, age, position, salary))
    # Execute the SQL query with parameters
    conn.commit()
    print("Employee added successfully.")


def view_employees():
    # Function to view all employees
    conn = conection()
    cursor = conn.cursor()
    sql = "SELECT * FROM Employees"
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        print(
            "-------------------------------------------------Employees information---------------------------------------------------------")
        print(
            f" ID : {row.id} \n Name : {row.name}\n Age : {row.age}\n Position : {row.position}\n Salary : {row.salary}")
        print(
            "---------------------------------------------------------------------------------------------------------------------------------")


def update_employee():
    # Function to update employee details
    conn = conection()
    cursor = conn.cursor()
    id = int(input("Enter employee ID to update: "))
    name = input("Enter employee name: ")
    age = int(input("Enter employee age: "))
    position = input("Enter employee position: ")
    salary = float(input("Enter employee salary: "))
    cursor.execute("UPDATE Employees SET name = ? , age = ?, position = ?, salary = ? WHERE id = ?",
                   (name, age, position, salary, id))
    conn.commit()
    print("Employee details updated.")


def delete_employee():
    # Function to delete an employee
    conn = conection()
    cursor = conn.cursor()
    id = int(input("Enter employee ID to delete: "))

    cursor.execute("DELETE FROM Employees WHERE id = ?", (id,))
    conn.commit()
    print("Employee deleted.")


def search_employee_by_name(name):

    # Connect to SQL Server
    conn = conection()
    cursor = conn.cursor()

        # Define SQL query to search for employees by name
    sql_query = "SELECT * FROM Employees WHERE name LIKE ?"

        # Execute the SQL query with parameter
    cursor.execute(sql_query, ('%' + name + '%',))

        # Fetch all matching rows
    rows = cursor.fetchall()

    if not rows:
        print(f"No employee with the name '{name}' found.")
    else:
        print(f"Employee(s) with the name '{name}':")
        for row in rows:
            print(
                    f"ID : {row.id}\nName : {row.name}\nAge : {row.age}\nPosition : {row.position}\nSalary: {row.salary}")



# Main program loop
while True:
    print("\nEmployee Management System")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Update Employee Details")
    print("4. Delete Employee")
    print("5. Search Employee")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        add_employee()
    elif choice == '2':
        view_employees()
    elif choice == '3':
        update_employee()
    elif choice == '4':
        delete_employee()
    elif choice == '5':
        employee_name = input("Enter the name of the employee to search for: ")
        search_employee_by_name(employee_name)
    elif choice == '6':
        break
    else:
        print("Invalid choice. Please try again.")
