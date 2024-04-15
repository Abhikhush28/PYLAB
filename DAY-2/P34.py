# Question 6:
 
# Longest and Shortest Words
# Given the list of words below ..
 
# word_list = ["apple", "airplane", "carrot", "elephant", "guitar", "moonlight"]
 
# … find the longest and the shortest word in the list.


word_list = ["apple", "airplane", "carrot", "elephant", "guitar", "moonlight"]

# Initialize variables to store the longest and shortest words
longest_word = word_list[0]
shortest_word = word_list[0]

# Loop through the list to find the longest and shortest words
for word in word_list:
    if len(word) > len(longest_word):
        longest_word = word
    elif len(word) < len(shortest_word):
        shortest_word = word

# Print the longest and shortest words
print("Longest Word:", longest_word)
print("Shortest Word:", shortest_word)
