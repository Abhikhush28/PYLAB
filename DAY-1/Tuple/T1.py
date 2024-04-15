# Program  that uses  tuples  to manages  a lists of employees:
# -------------------------------- Initialize  a list  of employee

employees = [
('John Doe', 'Manager', 50000),
('Jane Smith', 'Developer', 60000),
('Michael Johnson', 'Designer', 45000),
('Emily Brown', 'Analyst', 55000)
]


# print(type(employees))
# Function to Display  employee information
def display_employees():
 print("Employee Information:")
 for employee in employees:
  print(f"Name: {employee[0]}, Position: {employee[1]}, Salary: ${employee[2]}")

def add_employee(name, position, salary):
 employees.append((name, position, salary))
 print(f"{name} has been  added to the employee list.")


def remove_employee(name):
 for employee in employees:
  if name in employee:
   employees.remove(employee)
   print("The Employee has been remove")



# main program loop
while True:
 print("\n1. Add new employee")
 print("2. Display employee information")
 print("3. Remove the employee")
 print("4. Exit")

 choice = input("Enter your choice (1-4) :  ")
 if choice == '1':
  name = input("Enter Employee Name: ")
  position = input("Enter Employee Position: ")
  salary = input("Enter Employee Salary: ")
  add_employee(name, position, salary)
 elif choice == '2':
  display_employees()
 elif choice == '3':
  name = input("Enter the Employee name: ")
  remove_employee(name)
 elif choice == '4':
  print("Exiting Program...")
  break

 else:
  print("Invaild choice!!. Please Enter a Number  from 1 to 4")