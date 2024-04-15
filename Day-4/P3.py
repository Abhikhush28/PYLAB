# # # Time Complexity:
# # # Best Case: In the best case, the key might be present at the first index. So the best case complexity is O(1)
# # # Worst Case: In the worst case, the key might be present at the last index i.e., opposite to the end from which the search has started in the list. So the worst-case complexity is O(N) where N is the size of the list.
# # # Average Case: O(N)
 

# #  [10:03 AM] N Murugadoss (Unverified)
# # Time Complexity:
# # Best Case: In the best case, the key might be present at the first index. So the best case complexity is O(1)
# # Worst Case: In the worst case, the key might be present at the last index i.e., opposite to the end from which the search has started in the list. So the worst-case complexity is O(N) where N is the size of the list.
# # Average Case: O(N)
# # Auxiliary Space: O(1) as except for the variable to iterate through the list, no other variable is used. 
# # Advantages of Linear Search:
# # Linear search can be used irrespective of whether the array is sorted or not. It can be used on arrays of any data type.
# # Does not require any additional memory.
# # It is a well-suited algorithm for small datasets.
# # Drawbacks of Linear Search:
# # Linear search has a time complexity of O(N), which in turn makes it slow for large datasets.
# # Not suitable for large arrays.
# # When to use Linear Search?
# # When we are dealing with a small dataset.
# # When you are searching for a dataset stored in contiguous memory.



# # we have list
 
 
# # read x to search in the list [ x value must be found from the console ]
 
 
# # 1. if found, msg successufull and tell location by index
 
# # 2. if not found, msg unsuccessfull

# # sid =[1022,2345,5678,2378,9012,23]

# # x = int(input("Enter the Number for Search: "))

# # for i in sid:
# #  if i == x:
# #   print("Found ")
# #   break



# # sol -1
# # sid =[1022,2345,5678,2378,9012,23]
# # n=1022
# # for i in range(len(l)):
# #     if l[i]==n:
# #         print("sucessful",i)
# #         break
# # else:
# #     print("unsucessful")



# # [10:13 AM] Akhil Govind (Unverified)
# # sid =[1022,2345,5678,2378,9012,2364]
# # def search(x):
# #     for i in sid:
# #         if i == x :
# #             return "Successfully Found" , sid.index(i)
# #     else:
# #         return "Unsuccessful"    
 
# # val=int(input('Enter a number to search '))
# # search(val)
# # if search(val)[0]=="Successfully Found":
# #     print('Number is at',search(val)[1],'location')
# # else:
# #     print('Number is Not Found')



# # sid = [1022, 2345, 5678, 2378, 9012, 23]
 
# # def search_id(x):
# #     if x in sid:
# #         print("Successful! The value", x, "is found at index:", sid.index(x))
# #     else:
# #         print("Unsuccessful! The value", x, "is not found.")
 
 
# # x = int(input("Enter the value to search: "))
# # search_id(x)


# # sid = [1022, 2345, 5678, 2378, 9012, 23]
# # x = int(input("Enter a value to search for: "))
# # if x in sid:
# #     index = sid.index(x)
# #     print("Successful! Value found at index.", sid.index(x))
# # else:
# #     print("Unsuccessful. Value not found in the list.")


# # [10:17 AM] Jitendriya Jena (Unverified)
# # sid = [1022, 2345, 5678, 2378, 9012, 23]

# # x = int(input("Enter the value of x to search: "))

# # def search(x):

# #     if x in sid:

# #         index = sid.index(x)

# #         print(f"Successful! {x} found at index {index} .")

# #     else:

# #         print(f"Unsuccessful! {x} Not found.")
 
# # search(x)



# \[11:17 AM] N Murugadoss (Unverified)
# Q1. What are the two phases of Heap Sort?
# The heap sort algorithm consists of two phases. In the first phase, the array is converted into a max heap. And in the second phase, the highest element is removed (i.e., the one at the tree root) and the remaining elements are used to create a new max heap.
# [11:17 AM] N Murugadoss (Unverified)
# Q2. Why Heap Sort is not stable?
# The heap sort algorithm is not a stable algorithm because we swap arr[i] with arr[0] in heapSort() which might change the relative ordering of the equivalent keys.
# [11:19 AM] N Murugadoss (Unverified)
# Advantages of Heap Sort:
# Efficient Time Complexity: Heap Sort has a time complexity of O(n log n) in all cases. This makes it efficient for sorting large datasets. The log n factor comes from the height of the binary heap, and it ensures that the algorithm maintains good performance even with a large number of elements.
# Memory Usage – Memory usage can be minimal (by writing an iterative heapify() instead of a recursive one). So apart from what is necessary to hold the initial list of items to be sorted, it needs no additional memory space to work
# Simplicity –  It is simpler to understand than other equally efficient sorting algorithms because it does not use advanced computer science concepts such as recursion.
# Disadvantages of Heap Sort:
# Costly: Heap sort is costly as the constants are higher compared to merge sort even if the time complexity is O(n Log n) for both.
# Unstable: Heap sort is unstable. It might rearrange the relative order.
# Efficient: Heap Sort is not very efficient when working with highly complex data.
# 
# 
# 
# arr =[81,89,9,11,14,76,54,22]
 
# do sorting using heap sort.
 
# 1. arrange these elements into binary  tree
 
# 2. swap with parent if parent is less than its child nodes 




# https://leetcode.com/problemset/
 
# https://www.hackerrank.com/domains/python?filters%5Bdifficulty%5D%5B%5D=medium
 
# Codility - training
# https://app.codility.com/programmers/lessons/1-iterations/
# Codility - Test demo link
# https://app.codility.com/demo/take-sample-test/