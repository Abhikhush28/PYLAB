# The map() function in Python is used to apply a specified function to each item in an iterable (such as a list, tuple, etc.) and returns an iterator that yields the results. The syntax of the map() function is:


# Syntax :
# map ( function, iterable1, iterable2, ....)

# function : The  function to apply  to each  item  in the iterables(s)
 # iterable1, iterable2 etc,: One or More  iterable objects (e.g. lists, tuples,etc.) whose  items  will be  passed  to the function

 # Here's  a Simple  example  to illustarte  how map() works:
 # Define  a function to square a number
def square(x):
 return x**2

# Create a list of numbers
numbers = [1, 2, 3, 4, 5]

# Use map() to apply  the square function to each item  in the list
squared_number = map(square, numbers)

#Convert the iterator to a list to see the results
result = list(squared_number)
print(result)
