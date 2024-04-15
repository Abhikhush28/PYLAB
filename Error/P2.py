def divide_numbers(x,y):
 try:
  result = x/y
  print("Result of Division: ", result)
 except ZeroDivisionError:
  print("Error: Cannot divide by zero.")
 except ValueError:
  print("Error: Invaild input. Please enter vaild numbers.")
 except TypeError:
  print("Error: Unsupported operand type.")
 except Exception as e:
  print("An error occurred:", e)
 finally:
  print("This block always executes, regardless of exceptions")



# Main program 
divide_numbers(10, 2)
divide_numbers(10, 0)
divide_numbers("10", 2)