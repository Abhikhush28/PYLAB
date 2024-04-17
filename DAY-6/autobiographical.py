# An Autobiographical Number is a number N such that the first digit of N represents the 
# count of how many zeroes are there in N, the second digit represents the count of how 
# many ones are there in N and so on.
 
 
# You are given a function, def FindAutoCount(n):
# The function accepts string “n” which is a number and checks whether the number is an 
# autobiographical number or not. If it is, an integer is returned, i.e. the count of distinct 
# numbers in ‘n’. If not, it returns 0.
# Assumption:
# The input string will not be longer than 10 characters.
# Input string will consist of numeric characters.
# Note:
# If string is None return 0.
# Example:
# Input:
# n: “1210”
# Output:
# 3
# Explanation:
# 0th position in the input contains the number of 0 present in input, i.e., 1, in 1st position the 
# count of number of 1s in input i.e. 2, in 2nd position the count of 2s in input i.e. 1, and in 3rd 
# position the count of 3s i.e. 0, so the number is an autobiographical number.
# Now unique numbers in the input are 0, 1, 2, so the count of unique numbers is 3.


# def FindAutoCount(n):
#     if n is None:
#         return 0

#     digit_counts = [0] * 10  # Initialize an array to store counts of digits 0-9

#     for digit in n:
#         digit_counts[int(digit)] += 1  # Increment the count for each digit in the input

#     distinct_numbers = 0
#     for i, count in enumerate(digit_counts):
#         if count > 0:
#             distinct_numbers += 1  # Count the distinct numbers present in the input

#     return distinct_numbers if n == ''.join(str(digit_counts[i]) for i in range(10)) else 0

# # Example usage:
# input_str = "1210"
# output = FindAutoCount(input_str)
# print(output)  # Output: 3

 
