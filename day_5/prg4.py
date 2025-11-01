class Employee:
    # class variable
    employee_count = 0

    def __init__(self, name, designation, salary):
        self.name = name
        self.designation = designation
        self.salary = salary
        Employee.employee_count += 1  # update class variable

    def display_employee(self):
        print("Name:", self.name, "\tDesignation:", self.designation, "\tSalary:", self.salary)

employees = []

while True:
    print("\nEnter details of Employee", Employee.employee_count + 1)
    name = input("Enter name: ")
    designation = input("Enter designation: ")
    salary = float(input("Enter salary: "))
    employees.append(Employee(name, designation, salary))

    choice = input("Do you want to add another employee? (y/n): ")
    if choice.lower() != 'y':
        break

print("\n----- Employee Details -----")
for emp in employees:
    emp.display_employee()

print("\nTotal Number of Employees:", Employee.employee_count)