def linear_search(arr, target):
 for i in range(len(arr)):
  if arr[i] == target:
   return i
  
 return -1 # Target Not found


# Example usage:
my_list = [3, 6,8,2,9,1]
target_value = 8
result_index = linear_search(my_list, target_value)

if result_index != -1:
 print(f"Found at index {result_index}")
else:
 print("Not Found")