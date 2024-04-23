# Write a Python program to create a class and display the namespace of that class.
class py_solution:
 def sub_sets(self, sset):
  return self.sub_setsRecur([], sorted(sset))
 
 def sub_setsRecur(self, current, sset):
  if sset:
   return self.sub_setsRecur(current, sset[1:]) + self.sub_setsRecur(current + [sset[0]], sset[1:])
  
  return [ current]
 

for name in py_solution.__dict__:
 print(name)
