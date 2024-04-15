# name = "Abhishek"
# age = 30

# # formated_string =  "My name is {} and I am {} years old.".format(name, age)
# # print(formated_string)

# print(f"My name is {name} and I am {age} years old.")
# for x in range(-5, 0):
#  print(x)




# String Methods for Checking  and  Manipulating

my_string = "Hello, World!"


#Checking  if a string  starts or ends with  a  specifics  substring
print(my_string.startswith("Hello")) # Expected Output is True
print(my_string.endswith('World')) # Expected Output is False

# Replacing substrings
new_string = my_string.replace("Hello", "Hi")
print(new_string)

# Finding the index of a substring
index = my_string.find("World")
print(index)

# Checking  if  the String  contains only  digits
numeric_string = "12345"
print(numeric_string.isdigit())



# String Comparision
string1 = "hello"
string2 = "world"

# Comparing strings
print(string1 == string2)  # Expected Output: False
print(string1 != string2)  # Expected Output: True
print(string1< string2) # Output : True (lexicographical order comparision)


x = 10
y = 20
print(f"The sum of {x} and {y} is {x+y}.")


unicode_string = "Hello, 你好"

# Encode  to UTF-8
utf8_bytes = unicode_string.encode("utf-8")
print(utf8_bytes)

# Decode from UTF-8
decode_string = utf8_bytes.decode("utf-8")
print(decode_string)


