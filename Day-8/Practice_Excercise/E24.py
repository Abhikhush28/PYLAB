sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]
# Expected output:
# Note: Set is unordered.
# {'Green', 'Yellow', 'Black', 'Orange', 'Red', 'Blue'}

print(sample_set.union(set(sample_list)))