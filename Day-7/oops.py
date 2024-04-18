# [2:22 PM] N Murugadoss (Unverified)
class Person:  

    count = 0   # This is a class variable  

    def __init__(self, name, age):  

        self.name = name    # This is an instance variable  

        self.age = age      # This is an instance variable  

        Person.count += 1   # Accessing the class variable using the name of the class  
 
person1 = Person("Ayan", 25)  

person2 = Person("Bobby", 30)  
 
print(Person.count)     
 
 

