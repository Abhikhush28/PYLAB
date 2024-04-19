# List Slicing  is a common 
# format of list slicing
# Lst[Initail: End :IndexJump]
#Positive index start from 0 to len(Lst)-1
Lst = [50, 70, 30, 20, 90, 10, 50]
#Display Lst of all element
print(Lst[::])

#Negative index -1 represent the last element a to -len(Lst) represnt the first element
print(Lst[-len(Lst)::])
print(Lst[:-3])



# # Python 3 implementation
# # of simple method to find
# # print pairs with given sum.
 
# # Returns number of pairs
# # in arr[0..n-1] with sum
# # equal to 'sum'
 
 
# def printPairs(arr, n, sum):
 
#     # count = 0
 
#     # Consider all possible
#     # pairs and check their sums
#     for i in range(0, n):
#         for j in range(i + 1, n):
#             if (arr[i] + arr[j] == sum):
#                 print("(", arr[i],
#                       ", ", arr[j],
#                       ")", sep="")
 
 
# # Driver Code
# arr = [1, 5, 7, -1, 5]
# n = len(arr)
# sum = 6
# printPairs(arr, n, sum)
 
# # This code is contributed
# # by Smitha