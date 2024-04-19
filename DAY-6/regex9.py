import re

# Define a regex pattern
pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# Sample text to search
text = "Please contact me at john.doe@email.com or jane_doe123@email.co.uk"

# Use re.findall to extract email addresses
emails = re.findall(pattern, text)

# Print the extracted email addresses
print(emails)
