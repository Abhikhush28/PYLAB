def pcond(x):
    if x >=50:
       return x
 
marks=[28,36,40,50,12,60,80,9]
passlist=filter(pcond , marks)
print(marks)
print(list(passlist))