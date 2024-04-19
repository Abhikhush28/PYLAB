# # Python program to interchange first and last elements in a list

# Input : [12, 35, 9, 56, 24]
# Output : [24, 35, 9, 56, 12]

# Input : [1, 2, 3]
# Output : [3, 2, 1]

# first method
# def interChangeFirstLast(lst):
#  for i in range(len(lst)):
#   if i == 0:
#    tempt = lst[i]
#    lst[i] = lst[-1]
#    lst[-1] = tempt
   
#  return lst



a = [12, 35, 9, 56, 24]
# print(interChangeFirstLast(a))

def swapList(arr):
 tempt = arr[0]
 arr[0] = arr[-1]
 arr[-1] = tempt

 return arr


print(swapList(a))
