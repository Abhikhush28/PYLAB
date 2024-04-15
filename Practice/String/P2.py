my_strings = "Hello@ World!"
upper_case =  my_strings.upper()
lower_case = my_strings.lower()

# print(upper_case)
# print(lower_case)

word = my_strings.split("@")
# print(word)

joined_string = str("@").join(word)
print(joined_string)