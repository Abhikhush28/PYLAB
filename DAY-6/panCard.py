# # [2:18 PM] N Murugadoss (Unverified)
# import re
# txt = "The rain in Spain"
# x = re.search("Spain$", txt)  # $ is used to match at the end
# if x:
#   print("YES! We have a match!")
# else:
#   print("No match")

# import re
 
# txt = "The rain in Spain"
 
# #Find all lower case characters alphabetically between "a" and "m":
 
# x = re.findall("[a-m]", txt)
# print(x)



# import re
 
# txt = "hello planet"
 
# #Check if the string starts with 'hello':
 
# x = re.findall("^hello", txt)
# if x:
#   print("Yes, the string starts with 'hello'")
# else:
#   print("No match")




# import re
# def isValidPanCardNo(panCardNo):
# 	regex = "[A-Z]{5}[0-9]{4}[A-Z]{1}"
# 	p = re.compile(regex)
 
# 	if(panCardNo == None):
# 		return False
 
	
# 	if(re.search(p, panCardNo)):
# 		return True
# 	else:
# 		return False
 
# # Driver Code.
 
 
# # Test Case 1:
# str1 = "ARQPN1929C"
# print(isValidPanCardNo(str1))





import re
def isValidPanCardNo(panCardNo):
	regex = "[A-Z]{5}[0-9]{4}[A-Z]{1}"
	p = re.compile(regex)
 
	if(panCardNo == None):
		return False
 
	
	if(re.search(p, panCardNo)):
		return True
	else:
		return False
# Test Case 1:
str1 = "ARQPN1929C"
print(isValidPanCardNo(str1))
 
str1 = "BNZAA2318J"
print(isValidPanCardNo(str1))
# Test Case 2:
str2 = "23ZAABN18J"
print(isValidPanCardNo(str2))
# Test Case 3:
str3 = "BNZAA2318JM"
print(isValidPanCardNo(str3))
# Test Case 4:
str4 = "BNZAA23184"
print(isValidPanCardNo(str4))
# Test Case 5:
str5 = "BNZAA 23184"
print(isValidPanCardNo(str5))