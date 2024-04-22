class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity
 
class Bus(Vehicle):
    pass
 
School_bus = Bus("School Volvo", 12, 50)
 
# Python's built-in type()
print(type(School_bus))









# # Create a Vehicle class without any variables and methods
# # Create a Class with instance attributes
# # Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.

# class Vehicle:
#     def _init_(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage

#     def seating_capacity(self, capacity):
#      return f"The seating capacity of a {self.name} is {capacity } spassengers"

# class Bus(Vehicle):
#  pass

# School_bus = Bus("School Volvo", 180, 12)
# print("Vehicle Name:", School_bus.nsame, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)




# # Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
# # Given:


# # class Vehicle:

# #     def _init_(self, name, max_speed, mileage):
# #         self.name = name
# #         self.max_speed = max_speed
# #         self.mileage = mileage
# # Example of empty class
# # class Vehicle:
# #     pass






