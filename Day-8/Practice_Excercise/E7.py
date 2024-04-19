
# function of palindrome                 
def palindrome(a):
 mid = (len(a)-1)//2
 start =0
 last = len(a)-1
 flag = 1
 while(start<=mid):
  if (a[start] == a[last]):
   start += 1
   last -= 1
  else:
   flag = 0
   break

 if flag:
  print("The Enter String is Palindrome ")
 else:
  print("The entered  string  is not palindrome. ")



# function for symmetrical
def symmetry(a):
 n = len(a)
 flag =0

 

 


string = 'amaaya'
palindrome(string)