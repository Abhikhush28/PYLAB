# # Python dictionary with keys having multiple Inputs
# dict = {}

# x, y , z = 10,20,30
# dict[x,y,z] = x+y-z;

# x,y,z = 5,2,4
# dict[x,y,z] = x+y-z;


# print(dict)

# Python dictionary with keys having multiple inputs to get access to the keys. 

places = {
("19.07'53.2", "72.54'51.0"):"Mumbai",
("28.33'34.1", "77.06'16.6"):"Delhi"
}

print(places)
# Traversing dictionary with multi-keys and creating
# different lists from it

lat = [x[0] for x in places.keys()]
lon = [x[1] for x in places.keys()]
plc = [x for x in places.values()]

print(lat)
print(lon)
print(plc)




# Creating a dictionary with multiple inputs for keys
data = {
    (1, "John", "Doe"): {"a": "geeks", "b": "software", "c": 75000},
    (2, "Jane", "Smith"): {"e": 30, "f": "for", "g": 90000},
    (3, "Bob", "Johnson"): {"h": 35, "i": "project", "j": "geeks"},
    (4, "Alice", "Lee"): {"k": 40, "l": "marketing", "m": 100000}
}


print(data[1, "John", "Doe"]["a"])
print(data[2, "Jane", "Smith"]["f"])
print(data[3, "Bob", "Johnson"]["j"])


data[(1,"John", "Doe")]["a"] = {"b":"marketing", "c":75000}
print(data[1, "John", "Doe"]["a"])