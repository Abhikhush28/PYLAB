# [1:47 PM] N Murugadoss (Unverified) 
# price = 49
# txt = "The price is {} dollars"
# print(txt.format(price))

# quantity = 3
# itemno = 567
# price = 49
# myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
# print(myorder.format(quantity, itemno, price))



# age = 36
# name = "John"
# txt = "His name is {1}. {1} is {0} years old."
# print(txt.format(age, name))


#Set

# thisset = {"apple", "banana", "cherry", "apple"}
# print(thisset)
# thisset = {"apple", "banana", "cherry"}
# for x in thisset:
#   print(x)


# You can use the & operator instead of the intersection() method, and you will get the same result.
 
# Example
 
# Use & to join two sets:
 
# set1 = {"apple", "banana", "cherry"}
 
# set2 = {"google", "microsoft", "apple"}
 
# set3 = set1 & set2
 
# print(set3)
 
 
# ==================================================================================================
 
# Remove all elements from the fruits set:
 
# fruits = {"apple", "banana", "cherry"}
 
# fruits.clear()
 
# print(fruits)



# set1 = {"apple", "banana", "cherry"}
 
# set2 = {"google", "microsoft", "apple"}
 
 
# set3 = set1.intersection(set2)
 
# print(set3)



# thisset = {"apple", "banana", "cherry"}
 
# thisset.remove("banana")
 
# print(thisset)


# thisset = {"apple", "banana", "cherry"}
 
# mylist = ["kiwi", "orange"]
 
# thisset.update(mylist)
 
# print(thisset)


# Add elements from tropical into thisset:
 
# thisset = {"apple", "banana", "cherry"}
 
# tropical = {"pineapple", "mango", "papaya"}
 
 
# thisset.update(tropical)
 
# print(thisset)


# Write a Python program to remove an item from a set if it is present in the set.





# Create a new set 'num_set' with the elements 0, 1, 2, 3, 4, and 5 using a list:
 
num_set = set([0, 1, 2, 3, 4, 5])
 
# Remove an item [ item must be obtained from console ]   from a set if it is present in the set
print(num_set)
# print set before removing
x = int(input("Enter the Number: "))
if x in num_set:
 num_set.remove(x)
 print(num_set)
else:
 print("input number is not vaild")

# pint set after removing
