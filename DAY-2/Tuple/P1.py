# Get the number of elements in the tuple
n = int(input())

# Get the space-separated integers as input and convert them into a tuple
tuple_input = tuple(map(int, input().split()))

# Compute the result using the hash() function
result = hash(tuple_input)

# Print the result
print(result)
