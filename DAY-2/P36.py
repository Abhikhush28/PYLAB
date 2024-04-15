# Problem 10:
 
# Sorting a Mixed List
# Imagine you have a list with mixed data types: strings, integers, and floats:
 
mixed_list = ["apple", 5, 3.14, "banana", 7, 2.5, "orange", 10, 1.618, "grape"]
# Typically, you wouldn’t be able to sort this list, since Python cannot compare strings to numbers. However, writing a custom sorting function can help you sort this list.
 
# Create a function that sorts the mixed list above using the following logic:
 
# If the element is a string, the length of the string is used for sorting.
# If the element is a number, the number itself is used.

def custom_sort(x):
 strings = [x for x in mixed_list if isinstance(x, str)]
 numbers = [x for x in mixed_list if not isinstance(x, str)]

 #Sort the Strings based on the length
 strings.sort(key=len)

 # Sorts Number
 numbers.sort()


 #Combine the list
 sorted_list = strings + numbers
 return sorted_list


# Example Usage
sorted_list = custom_sort(mixed_list)
print(len(sorted_list))