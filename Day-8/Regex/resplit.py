import re 
# target_string = "My name is maximums and my luck numbers are 12 45 78"
# # split on white-space 
# word_list = re.split(r"\s+", target_string) 
# print(word_list)
# ==================================
# target_string = "12-45-78"

# # Split only on the first occurrence
# # maxsplit is 1
# result = re.split(r"\D", target_string, maxsplit=1)
# print(result)
# # Output ['12', '45-78']

# # Split on the three occurrence
# # maxsplit is 3
# result = re.split(r"\D", target_string, maxsplit=3)
# print(result)
# # Output ['12', '45', '78']


# target_string = "12,45,78,85-17-89"
# # 2 delimiter - and ,
# # use OR (|) operator to combine two pattern
# result = re.split(r"-|,", target_string)
# print(result)
# # Output ['12', '45', '78', '85', '17', '89']



target_string = "PYnative   dot.com; is for, Python-developer"
# Pattern to split: [-;,.\s]\s*
result = re.split(r"[-;,.\s]\s*", target_string)
print(result)
# Output ['PYnative', 'dot', 'com', 'is', 'for', 'Python', 'developer']