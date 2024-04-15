paul_friends = ["Mary", "Tim", "Mike", "Henry"]
tina_friends = ["Tim", "Susan", "Mary", "Josh"]
 
# Combine both lists into a single list that contains all of their friends. 
# Don’t include duplicate entries in the resulting list.


# Combine both lists into a single list and remove duplicates using set
combined_friends = list(set(paul_friends + tina_friends))

print("Combined Friends List:", combined_friends)
