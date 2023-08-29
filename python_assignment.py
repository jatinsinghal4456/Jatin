class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeDatabase:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def search_by_age(self, target_age):
        matching_employees = [e for e in self.employees if e.age == target_age]
        return matching_employees

    def search_by_name(self, target_name):
        matching_employees = [e for e in self.employees if e.name == target_name]
        return matching_employees

    def search_by_salary(self, operator, target_salary):
        if operator == '>':
            matching_employees = [e for e in self.employees if e.salary > target_salary]
        elif operator == '<':
            matching_employees = [e for e in self.employees if e.salary < target_salary]
        elif operator == '>=':
            matching_employees = [e for e in self.employees if e.salary >= target_salary]
        elif operator == '<=':
            matching_employees = [e for e in self.employees if e.salary <= target_salary]
        else:
            raise ValueError("Invalid operator. Use '>', '<', '>=', or '<='.")

        return matching_employees

    def print_employees(self, employees):
        for employee in employees:
            print(f"Name: {employee.name}, Age: {employee.age}, Salary: {employee.salary}")

if __name__ == "__main__":
    database = EmployeeDatabase()

    # Add some employees to the database
    database.add_employee(Employee("Raman", 41, 56000))
    database.add_employee(Employee("Himadri", 38, 67500))
    database.add_employee(Employee("Jaya", 51, 82100))
    database.add_employee(Employee("Tejas", 30, 55000))
    database.add_employee(Employee("Ajay", 45, 44000))
    # User input for search
    print("Choose a search parameter:")
    print("1. Age")
    print("2. Name")
    print("3. Salary (>, <, <=, >=)")
    choice = input("Enter your choice: ")

    if choice == "1":
        target_age = int(input("Enter the age to search for: "))
        result = database.search_by_age(target_age)
    elif choice == "2":
        target_name = input("Enter the name to search for: ")
        result = database.search_by_name(target_name)
    elif choice == "3":
        operator = input("Enter the operator (> < >= <=): ")
        target_salary = int(input("Enter the salary to compare: "))
        result = database.search_by_salary(operator, target_salary)
    else:
        print("Invalid choice")

    if result:
        print("Search results:")
        database.print_employees(result)
    else:
        print("No matching records found.")
