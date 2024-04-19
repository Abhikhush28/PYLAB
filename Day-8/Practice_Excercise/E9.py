# Remove empty strings from the list of strings
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

def remove_empty_strings(list1):
    return [string for string in list1 if string]

print(remove_empty_strings(list1))


