# [3:40 PM] N Murugadoss (Unverified)
# Write a Python function that filters out elements from a list of strings containing a specific substring using the filter function.
 
strings = ["Red", "Green", "Orange", "White", "Black", "Pink", "Yellow"]

substring = "l"
print(list(filter(lambda x: substring in x, strings)))
