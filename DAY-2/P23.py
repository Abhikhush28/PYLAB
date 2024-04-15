# # Create two lists named 'nums1' and 'nums2' containing integer elements
# num1 = [6, 5, 3, 9]
# num2 = [0, 1, 7, 7]
 
# # Result:
 
# # [(6, 6), (6, 4), (10, -4), (16, 2)]

# index =0
# for i in num1:
#   x = i + num2[index]
#   y = i -  num2[index]

# print(list(zip(num1, num2)))




# Create two lists named 'nums1' and 'nums2' containing integer elements
num1 = [6, 5, 3, 9]
num2 = [0, 1, 7, 7]
 
# Define a function named addition_subtrction that performs addition and subtraction on two numbers
 
def addition_subtrction(x, y):
    return x + y, x - y
 
# Create two lists named 'nums1' and 'nums2' containing integer elements
 
nums1 = [6, 5, 3, 9]
nums2 = [0, 1, 7, 7]
 
result = map(addition_subtrction, nums1, nums2)
 
print(list(result))
 