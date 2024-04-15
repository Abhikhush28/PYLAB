def max_sum_subarray(arr):
 max_sum = float('-inf')   # Initialize max_sum to negative infinity
 current_sum = 0 # Initialize current_sum to 0

 for num in arr:
  current_sum = max(num, current_sum+num)
  max_sum = max(max_sum, current_sum)

 return max_sum