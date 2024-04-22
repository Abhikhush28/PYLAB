# Reverse Words in a Given String in Python

# Examples:

# Input : str =" geeks quiz practice code"
# Output : str = code practice quiz geeks  
# Input : str = "my name is laxmi"
# output : str= laxmi is name my 

str =" geeks quiz practice code"

# Explaination:

# 1. Split the string into words
# 2. Reverse each word
# 3. Join the words
    
print(" ".join(str.split()[::-1]))
