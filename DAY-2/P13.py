# [10:56 AM] N Murugadoss (Unverified)
# Write a Python program to calculate the sum of the positive and negative numbers
 
# of a given list of numbers using the lambda function.
 
# Create a list named 'nums' containing integers, including both positive and negative numbers
 
nums = [2, 4, -6, -9, 11, -12, 14, -5, 17]


sumofpos = sum(filter(lambda x: x>0, nums))
sumofneg = sum(filter(lambda x: x<0, nums))

print("sum Of Positive: ",sumofpos)
print("sume of Negative: ", sumofneg)