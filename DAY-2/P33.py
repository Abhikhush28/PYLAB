# Question 5:Calculate the Statistics
 
# Given any list of numbers in Python, such as …
 
numbers = [10, 3, 5, 9, 18, 3, 0, 7]
# … write a function that returns a tuple containing the list’s maximum value, sum of values, and mean value.

def Statistics(numbers):
 max_value = max(numbers)
 sum_value = sum(numbers)
 mean_value = sum_value/len(numbers)

 return max_value, sum_value, mean_value

print(tuple(Statistics(numbers)))