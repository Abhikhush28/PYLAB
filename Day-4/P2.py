# [9:31 AM] N Murugadoss (Unverified)
# Task 1 :
 
# create class student contains name, age , marks1 and marks2.
 
# create method displayInfo() : to display name, age, marks1 , marks2  , total and avg
 
# create method findTotalAvg() to find total of marks1 , marks2 and its average.
 
# create two objects s1 and s2.
 
# pass values name, age ,marks1 and marks2

class student:
 def __init__(self, name, age, marks1, marks2):
  self.name = name
  self.age = age
  self.marks1 = marks1
  self.marks2 = marks2
 
 def displayInfo(self):
  print("Name: ", self.name)
  print("Age: ", self.age)
  print("Marks1: ", self.marks1)
  print("Marks2: ", self.marks2)

 def findTotalAvg(self):
  print("Total: ", self.marks1 + self.marks2)
  print("Average: ", (self.marks1 + self.marks2)/2)



stu1 = student("Abhishek", 20, 98, 89)
stu1.displayInfo()
stu1.findTotalAvg()

stu2 = student("Abhijit", 18, 70, 80)
stu2.displayInfo()
stu2.findTotalAvg()