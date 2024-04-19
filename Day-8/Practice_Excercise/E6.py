# Find Maximum of two numbers in Python

# Input: a = 2, b = 4
# Output: 4

# Input: a = -1, b = -4
# Output: -1



# First method using native
# def maximum(a, b):
#  if a<b:
#   return a
#  else:
#   return b


a = 2
b =4
# print(maximum(a, b))


# using max method
print(min(a, b))

# using trunary operator
print(a if a<= b else b)

#using lambda function

minmum = lambda a, b : a if a<b else b

print(minmum(a, b))