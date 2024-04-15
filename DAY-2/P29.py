# # Find the Common Friends
 
# # Now, let’s try a different operation. We will start from the same lists of Paul’s and Tina’s friends:
# # paul_friends = ["Mary", "Tim", "Mike", "Henry"]
# # tina_friends = ["Tim", "Susan", "Mary", "Josh"]
# # print(set(paul_friends).intersection(set(tina_friends)))




# Question 3:
# Find the Basketball Players
# You work at a sports club. The following sets contain the names of players registered to play different sports:
football_players = {"Eve", "Tom", "Richard", "Peter"}
volleyball_players = {"Jack", "Hugh", "Peter", "Sam"}
basketball_players = {"Eve", "Richard", "Jessica", "Sam", "Michael"}

# How can you obtain a set that includes the players that are only registered to play basketball (i.e. not registered for football or volleyball)?

print(list(filter(lambda x: x not in set(football_players.union(volleyball_players)), basketball_players)))












 

 

 
 

 
 

 
 
# Question 7:
 
# Filter a List by Frequency
# Given a list of numbers …
 
# number_list = [5, 8, 2, 7, 3, 5, 6, 9, 2, 4, 8, 7, 1, 5, 3]
 
# … create a new list containing only the numbers that occur at least three times in the list.
 
 
# Question 8:
 
# The Second-Best Score
 
# You’re given a list of students’ scores in no particular order:
 
# exam_results = [23, 78, 96, 32, 53, 67, 23, 98, 33, 38, 45, 39, 86, 12, 43, 45]
 
# Find the second-highest score in the list.
 
# Question 9: Check If a List Is Symmetrical
# Given the lists of numbers below …
 
# list_one = [1, 2, 3, 2, 1]
# list_two = [1, 1, 2, 2, 3]
 
# … create a function that returns whether a list is symmetrical. 
# In this case, a symmetrical list is a list that remains the same after it is reversed – 
# i.e. it’s the same backwards and forwards.
 
 
# Problem 10:
 
# Sorting a Mixed List
# Imagine you have a list with mixed data types: strings, integers, and floats:
 
# mixed_list = ["apple", 5, 3.14, "banana", 7, 2.5, "orange", 10, 1.618, "grape"]
# Typically, you wouldn’t be able to sort this list, since Python cannot compare strings to numbers. However, writing a custom sorting function can help you sort this list.
 
# Create a function that sorts the mixed list above using the following logic:
 
# If the element is a string, the length of the string is used for sorting.
# If the element is a number, the number itself is used.