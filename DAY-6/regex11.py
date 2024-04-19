import re 
txt = "The rain in Spain"
x  = re.findall("[arn]", txt)

print(x)