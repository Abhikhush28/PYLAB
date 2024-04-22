# Create a dictionary by extracting the keys from a given dictionary
# Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.

# Given dictionary:

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# # Keys to extract
# keys = ["name", "salary"]

# Expected output:

# {'name': 'Kelly', 'salary': 8000}

# print(dict({x,y}) for x, y in sample_dict)





# sampleDict = { 
#   "name": "Kelly",
#   "age":25, 
#   "salary": 8000, 
#   "city": "New york" }

# keys = ["name", "salary"]

# newDict = {k: sampleDict[k] for k in keys}
# print(newDict)





# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"}

# # keys to extract
# keys = ["name", "salary"]

# # new dict
# res = dict()

# for k in keys:
#     # add current key with its va;ue from sample_dict
#     res.update({k: sample_dict[k]})
# print(res)




# ============================= Another =========================

# Delete a list of keys from a dictionary
# Given:

# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
# }

# # Keys to remove
keys = ["name", "salary"]
# Expected output:

# {'city': 'New york', 'age': 25}


for key in sample_dict:
 if key in keys:
  del sample_dict[key]
 

print(sample_dict)