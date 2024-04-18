# def myfunc():
#   x = 300
#   print(x)
# myfunc()
# print(x)

# # [9:16 AM] N Murugadoss (Unverified)
# def myfunc():
#   x = 300
#   def myinnerfunc():
#     print(x)
#   myinnerfunc()
# myfunc()


def myfunc():
  global x
  x = 300
myfunc()
print(x)