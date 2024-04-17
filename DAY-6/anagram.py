# Write a function isAnagrams () to validate if the provided two strings are anagrams or not.
 
# If  the two strings are anagrams, then return ‘Anagrams'.
 
# Otherwise, return ‘Word is not anagrams'.
 
# Words Example: race and care, listen and silent


# [9:19 AM] N Murugadoss (Unverified)
# def Anagrams(s1,s2):

#     s1=s1.replace('','').lower()

#     s2=s2.replace('','').lower()

#     if len(s1)!=len(s2):

#         return 'Word is not anagrams'

#     if sorted(s1) == sorted(s2):

#         return 'Anagrams'

#     else:

#         return 'Word is not anagrams'
 
# Anagrams('race','care')
 
 

def isAnagrams(str1, str2):
 str1 = str1.strip().lower()
 str2 = str2.strip().lower()
 if sorted(str1) == sorted(str2):
  return True
 else:
  return False

str1 = input("Enter the str1: ")
str2 = input("Enter the str2: ")

if isAnagrams(str1, str2):
 print("Anagrams")
else:
 print("Not Anagrams")