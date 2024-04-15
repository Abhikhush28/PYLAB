x = [1,2,3,4,5,6,7,8,9,10]

def xeven(x):
 if x  % 2 == 0:
  return x

def xodd(x):
 if x  % 2 == 0:
  pass
 else:
  return x

noseven = filter(xeven, x)

print("even: ", list(noseven))
nosodd = filter(xodd, x)
print("odd: ", list(nosodd))