# Merge two Python dictionaries into one
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# Expected output:

# {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}


# for key, value in dict2.items():
#     dict1[key] = value
  
# print(dict1)

# dict1.update(dict2)
# print(dict1)

# dict3 = dict(zip(dict1, dict2))
# print(dict3)


# print(dict1 | dict2)

# dict3 = dict1.copy()
# dict3.update(dict2)
# print(dict3)


dict3={**dict1 , **dict2}
print(dict3)