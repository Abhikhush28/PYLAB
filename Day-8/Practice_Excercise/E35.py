# Exercise 8: Rename key of a dictionary
# Write a program to rename a key city to a location in the following dictionary.

# sample_dict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"
# }

# sample_dict['location'] = sample_dict.pop('city')
# print(sample_dict)






# Exercise 9: Get the key of a minimum value from the following dictionary
sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}

# # values_list = [x for x in sorted(sample_dict.values())]

# # for key in sample_dict:
# #  if sample_dict[key] == values_list[0]:
# #   print(key)

# print(min(sample_dict.values()))
# print(min(sample_dict, key=sample_dict.get))




# Exercise 10: Change value of a key in a nested dictionary
# Write a Python program to change Brad’s salary to 8500 in the following dictionary.

# Given:

# sample_dict = {
#     'emp1': {'name': 'Jhon', 'salary': 7500},
#     'emp2': {'name': 'Emma', 'salary': 8000},
#     'emp3': {'name': 'Brad', 'salary': 500}
# }

# sample_dict['emp3']['salary'] = 8500


# print(sample_dict)