# We can also use map() with  multiple iterable and a function that  take  multiple arguments. For  example:

# define  a function to add two numbers
def add(x, y):
 return x+y


# Create two list of numbers
number1 = [1,2,3]
number2 = [4,5,6]


# use map() to apply the add function to corresponding  items in the lists
sums = map(add, number1, number2)

print(list(sums))