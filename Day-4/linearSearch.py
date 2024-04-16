# Algorithm of Linear_Search

# Linear_Search(a, n, val) // 'a' is the given array, 'n' is the size of given array, 'val' is the value to search  
# Step 1: set pos = -1  
# Step 2: set i = 1  
# Step 3: repeat step 4 while i <= n  
# Step 4: if a[i] == val  
# set pos = i  
# print pos  
# go to step 6  
# [end of if]  
# set ii = i + 1  
# [end of loop]  
# Step 5: if pos = -1  
# print "value is not present in the array "  
# [end of if]  
# Step 6: exit  
 

# LinearSearch(list, key):  
#  for each item in the list: 
#     if item == value  
#       return its index position  
#    return -1  
 

# [4:55 PM] N Murugadoss (Unverified)
def linear_Search(list1, n, key):  
  
    # Searching list1 sequentially  
    for i in range(0, n):  
        if (list1[i] == key):  
            return i  
    return -1  
  
  
list1 = [1 ,3, 5, 4, 7, 9]  
key = 7  
  
n = len(list1)  
res = linear_Search(list1, n, key)  
if(res == -1):  
    print("Element not found")  
else:  
    print("Element found at index: ", res)  