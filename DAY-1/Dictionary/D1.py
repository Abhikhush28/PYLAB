#Creating a Dictionary

my_dict = {
'name':'Abhsihek', 
'age':30, 
'city':'New York'
}

# print(my_dict)
#Accessing the Value of an Element in
print(my_dict['name'])

# Adding and Updating items
my_dict['email'] = 'alice@example.com'

my_dict['age'] = 35

del my_dict['city'] # remove  the key  'city'  from the dictionary
my_dict.pop('email')
print(my_dict)



for key in my_dict:
 print(key)


for value in my_dict.values():
 print(value)




for key , value in my_dict.items():
 print(f"{key}: {value}")





# dictionary comprihensions:

# Dictionary  comphrensions in python allow  you to create  dictionary  in a  consise and readable way  using  a single line of code .
# They  are similier  to list  comprehensions but  produice dictionary  instead  of list.

# The Synatx  for  dictionary comprehensions is {'Key_Expression: value_ Expression for item in itrable}


# Create  a dictionary  mapping  even  numbers  to their squares
# squares_dict = {
# x: x**2 
# for x in range(1,6)
# if x % 2 == 0}
# print(squares_dict)


number_classification = {x: 'even' if x %2 == 0 else 'odd' for x in range(1, 6)}
print(number_classification)