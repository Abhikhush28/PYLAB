# py P9.py 12 23 45 66
 
# print maximum value of passed arguments
 
# max is   66


import sys
n = len(sys.argv)
print("Total arguments passed:", n)
print("\nArguments passed:", end = " ")
num = []
for i in range(1, n):
   num.append(int(sys.argv[i]))

num = sorted(num)
print("Maximum Value is ", num[len(num)-1])
