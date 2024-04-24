class Student:
 def __init__(self, name , id):
  self.name = name
  self.id = id
  self.courses_taken = []


 def enroll(self, course):
  self.courses_taken.append(course)
 
 def drop(self, course):
  self.courses_taken.remove(course)
 
 def view_courses(self):
  print(f"{self.name}'s courses: {self.courses_taken}")


class Course:
 def __init__(self, title, instructor, max_students):
  self.title = title
  self.instructor = instructor
  self.max_students = max_students
  self.students_enrolled = []
 
 def add_student(self, student):
  if len(self.students_enrolled)< self.max_students:
   self.students_enrolled.append(student)
   student.enroll(self)
  else:
   print("Course is full")
  
 def drop_student(self, student):
  student.drop(self)
  self.students_enrolled.remove(student)

 def view_student(self):
  print(f"Student in {self.title}: {self.students_enrolled}")





math101 =  Course("Calculus", "Dr. Smith", 3)
john = Student("Jone Doe", "12345")
jane = Student("Jane Doe", "67890")


math101.add_student(john)
math101.add_student(jane)

john.view_courses()

math101.view_student()
