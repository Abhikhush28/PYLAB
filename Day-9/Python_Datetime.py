# Python Datetime class
# The  DateTime class contains information on both  date and time.

from datetime import datetime

a = datetime(1999, 12, 12)
print(a)

a = datetime(1999, 12,12 , 12, 12,12,342356)
print(a)

# Get year, month, hour, minute, and timestamp
print("year : ", a.year)
print("month : ", a.month)
print("hour : ", a.hour)
print("mintue : ", a.minute)
print("timestamp : ", a.timestamp())


# Current date and time
today = datetime.now()
print("Current date and time is ", today)

# Convert Python Datetime to String
string = datetime.isoformat(today)
print(string)
print(type(string))




