class Factorial:
 def __init__(self):
  pass

def fact1(x): 
    if x == 1:
        return 1
    else:
      return (x * fact1(x-1))
  