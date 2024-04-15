# # # Sets in Python are unordered collections of unique elements. This  means  that a  set can  only  contain unique values,  and the  order  of elements in a set  is not guranteed. set  are mutable  which means  you can  add or remmove  elements  from  them. Sets are defined  using  curly  braces '{}', and  elements are seperated  by commas.


# # # Creating empty Set
# # empty_set = set()


# # # Creating  a set  with elements
# # my_set = {1, 2, 3, 4, 50}
# # # print(my_set)

# # # Creating  a set from a list
# # my_list = [1,2, 2, 3, 4, 4,5]  # Duplicate  element removed
# # set_from_list = set(my_list)
# # print(set_from_list)

# # # print(list(set_from_list))

# # # Adding elements
# # my_set.add(60)

# # my_set.remove(50)
# # my_set.discard(60)

# # print(my_set)



# # Squaring numbers using lambda and map
numbers = [1, 2, 3, 4, 5]
# squared_numbers = list(filter(lambda x: x % 2 ==0 , numbers))
# print(squared_numbers)  # Output: [1, 4, 9, 16, 25]


# print({x ** 2 for x in range(1,6)})

even = filter(lambda x: "Even" if x%2 ==0 else "Odd", numbers)
print(list(even))