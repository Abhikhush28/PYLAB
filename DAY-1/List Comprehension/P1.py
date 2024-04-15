# 1. Square Numbers:
# numbers = [1,2,3,4,5]
# squared_numbers = [num ** 2 for num in numbers]
# print(squared_numbers)

# 2. Even Numbers in a Range:
# start =1
# end = 10
# even_numbers = [num for num in range(start, end+1) if num % 2 == 0]
# print("Even Numbers:", even_numbers)

# 3. List of Strings in Uppercase:
# words = ['hello', 'world', 'python']
# uppercase_words = [word.upper() for word in words]
# print(uppercase_words)

# 4. Extracting Vowels from a String:
# sentence = "hello world"
# vowels = [char for char in sentence if char.lower() in 'aeiou']
# print(vowels)


# 5. Matrix Transpose:
# matrix = [[1,2,3], [4,5,6], [7, 8, 9]]
# transpose_matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
# print("Transpose Matrix: ", transpose_matrix)

# 6. Flatten Nested Lists:
# nested_lists = [[1,2],[3,4],[5,6]]
# flattened_list = [item for sublist in nested_lists for item in sublist]
# print("Flattened List: ", flattened_list)


# 7. Filtering Prime Numbers: 
# Dought in all method
# numbers = [2,3,4,5,6,7,8,9,10]
# primes = [num for num in numbers if all(num % i !=0 for i in range(2, int(num ** 0.5) + 1))]
# print("Prime Numbers: ", primes)

# 8. List of Squares and Cubes:
# numbers = [1,2,3,4,5]
# squares_and_cubes = [(num, num**2, num**3) for num in numbers]
# print("Squares and Cubes: ", squares_and_cubes)

# 9. Combining Two Lists:
# list1 = ['a', 'b', 'c']
# list2 = [1,2,3]
# combined_list = [{x, y} for x in list1 for y in list2]
# print(combined_list)

# 10. Filtering Duplicates from a List:

numbers = [1, 2, 3, 2, 4, 5, 3, 6, 7]
unique_numbers = list(set(numbers))
print("Unique Numbers: ", unique_numbers)