# Exercise 5: Generate random String of length 5
import random
import string

letters = string.ascii_letters
random_string = ''.join(random.choice(letters) for _ in range(5))
print(random_string)