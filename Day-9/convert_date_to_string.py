# Convert Date to String
from  datetime import date

# calling  the today()
# function of date  class
today = date.today()

Str = date.isoformat(today)

print("String representation: ", Str)
print(type(today))
print(type(Str))

