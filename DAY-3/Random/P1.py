# random.randrange(start, stop, step)

# Exercise 1: Generate 3 random integers between 100 and 999 which is divisible by 5

import random
print("Generating  3 random  integers number between  100 and 999 divisible by 5")
for num in range(3):
 print(random.randrange(100, 999, 5), end=", ")