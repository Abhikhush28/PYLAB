# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"}

# # Keys to extract
# keys = ["name", "salary"]

# res = {x: sample_dict[x] for x in keys if x in sample_dict}
# print(res)



sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]

# res = {x: sample_dict[x] for x in sample_dict if x not in keys}
for x in keys:
 sample_dict.pop(x)

print(sample_dict)

