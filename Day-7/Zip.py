names = ['Alice', 'Bob', 'Charlie']  
ages = [25, 30, 35]  
heights = [160, 175, 180]  
# We can combine these three lists using the zip() function:  
combined = zip(names, ages, heights)  
# Now, we can iterate over the combined iterable and print out the tuples containing the name, age, and height of each person:  
for name, age, height in combined:  
    print(name, age, height)  