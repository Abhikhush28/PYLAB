# A program  that uses  tuples  to store  information about  student  and theirs grades and  then calculates  the avarages  grade for each student

students =  [
('John Doe', [85,90,92,88]),
('Jane Smith',[76,84,91,93]),
('Alice Johnson',[94,92,88,90]),
('Abhishek Kumar', [90,96,92,94])
]

# Function to calculate the average grade for a student
def calculate_average_grades(student):
 grades = student[1] # Accessing  the grades  from the tuple
 avarage_grade = sum(grades)/len(grades)
 return avarage_grade


# Function  to Display  student information and average  grades
def display_students():
 print("Student Information and Average Grades: ")
 if not students:
  print("Stduent Information is Empty ")
 else:
  for student in students:
   name = student[0]
   avarage_grade = calculate_average_grades(student)
   print(f"Name: {name}, Grades: {student[1]}, Average Grades: {avarage_grade:.2f}")


 

# Function to add the student details
def add_student(name , grades):
 students.append((name, grades))
 print("Student Added successfully")


# grades function
def input_grades():
    num = 4  # Number of grades to input
    grades = []  # List to store the grades

    for i in range(num):
        grade = input("Enter grade: ")
        grades.append(grade)

    return grades

# Main program Loop
while True:
 print("\n1. Display student information and average grades")
 print("2. Add the Student: ")
 print("3. Exit")

 choice = input("Enter your choice (1-2): ")

 if choice == '1':
  display_students()
 elif choice == '2':
  name = input("Enter the name of student: ")
  grades = input_grades()
  add_student(name, grades)
 elif choice == '3':
  print("Exiting Program...")
  break
 else:
  print("Invaild choice. Please enter a number  from 1 to 2.")