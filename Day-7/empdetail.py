class Person:  
    company ="Wipro , Bangalore"
    def __init__(self, name, age):  
        self.name = name    # This is an instance variable  
        self.age = age      # This is an instance variable  
    def displayInfo(self):
       print("\nName  = " , self.name)
       print("Age   = " , self.age)
       print("Company=" , Person.company)
p1 = Person("Abhishek", 25)  
p2 = Person("Abhijit", 30)  
p1.displayInfo()
p2.displayInfo()