import re

# Define a regex pattern for phone numbers
pattern = r'\b(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\b'

# Sample text containing phone numbers
text = """
John's phone number is +1 (555) 123-4567, and Jane's number is 123-456-7890.
Another contact is +91 9876543210, and an office line is (555) 987 6543 ext 1234.
"""

# Use re.findall to extract phone numbers
phone_numbers = re.findall(pattern, text)

# Print the extracted phone numbers
for match in phone_numbers:
    country_code, area_code, number, extension = match[:4]
    print(f"Country Code: {country_code}, Area Code: {area_code}, Number: {number}, Extension: {extension}")
