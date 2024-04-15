# Create a list 'weekdays' containing the names of the days of the week
 
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
 
# Use the 'filter()' function with a lambda function to filter days with a length of 6 characters
# The lambda function checks the length of each day and keeps only the days with a length of 6
# Empty strings ('') are filtered out to keep only days with a length of 6 characters


days  = filter(lambda x: len(x) == 6, weekdays)
print(list(days))
 