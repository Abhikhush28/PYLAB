# Python Time  class
# The time  class create the time  object which  represents local time, independent of any  day

# Constructor Syntax:
# class datetime.time(hour=0, minute=0, second=0, microsecond=0 tzinfo=None, *, fold=0)



# All the arguments are optional. tzinfo can be None Otherwise all the attributes must be  integer in the following range-

# 0 <= hour<24
# 0 <= minute <60
# 0 <= second <60
# 0 <= microsecond <1000000
# fold in [0,1]



# Example 1: Time Object  represents time in Python
from datetime import time

# calling the constructor
my_time = time(13, 24, 56)
print("Entered time", my_time)

# Calling the constructor with 1 argument
my_time = time(minute=12)
print("\nTime with one argument", my_time)


#calling constructor with 0 argument
my_time = time()
print("\nTime without argument", my_time)


my_time = time(11,34,56)

# Get hours, Minutes, seconds and microseconds
print("hour = ", my_time.hour)
print("minute = ", my_time.minute)
print("second = ", my_time.second)
print("microSecond = ", my_time.microsecond)


print("second = ", my_time.second)



# Convert Time  object to String
my_time = time(12, 24, 36, 1212)
str = my_time.isoformat()
print("String Representation:", str)
print(type(str))