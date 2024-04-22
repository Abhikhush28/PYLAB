# string = input("Enter the String: ")
# lst = string.split()
# print(lst)

# n = int(input("Enter the size of list: "))
# lst = list(map(int, input("Enter the integer\
#  elemenets: ").strip().split()))[:n]
# print("The list is: ", lst)


# List = [1,2,4,5,6]
# print(List)

# List.insert(2, 35)
# print(List)

# List.insert(0, 'Geeks')
# print(List)


# List = [1,2,45,67]
# print(List)

# List.extend([8, 'Abhsihek', 'Kumar'])
# print(List)

# mylist = [1, 2, 3, 4, 5, 'Geek', 'Python'] 
# mylist.reverse() #reverse method
# print(mylist)




# my_list = [1, 2, 3, 4, 5] 
# reverse_list = list(reversed(my_list))
# print(reverse_list)




# Python program to demonstrate 
# Removal of elements in a List 
  
# Creating a List 
# List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] 
# print(List)

# List.remove(5)
# List.remove(6)
# print(List)



# List Comprehension
# newLists = [expression(element) for element in oldList if condition]


# odd_square = [x**2 for x in range(1, 11) if x % 2 == 1]
# even_square = [x**2 for x in range(1,11) if x % 2 == 0]
# print(odd_square)
# print(even_square)

odd_square = []
for x in range(1, 11):
 if x %2 == 1:
  odd_square.insert(x-1, x**2)
 

print(odd_square)