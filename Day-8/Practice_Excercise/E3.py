staff=[ ('a', 45) ,('c', 35) , ('b', 55) ]
 
# sorted by on marks . sorting is done based on second item
 
# output we want
 
# [ ('c',35) , ('a',45) ,('b',55)]
# students = [
#     {'name': 'John', 'age': 20},
#     {'name': 'Alice', 'age': 18},
#     {'name': 'Bob', 'age': 22}
# ]

print(sorted(staff, key = lambda x : x[1]))