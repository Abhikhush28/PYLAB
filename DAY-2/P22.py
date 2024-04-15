# [2:31 PM] N Murugadoss (Unverified)
# Write a Python program to convert all the characters into uppercase  and
 
# eliminate duplicate letters from a given sequence. Use the map() function.
chrars = {'a', 'b', 'E', 'f', 'a', 'i', 'o', 'U', 'a'}
print(set(map(str.upper, chrars)))