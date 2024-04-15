# Try Block: The code that might raise an exception is placed inside the try block.
# Except Block: If an exception occurs in the try block, the code inside the except block is executed. The except block can specify the type of exception to catch, or it can catch all exceptions by using a generic except block.

# Finally Block (Optional): The finally block, if included, is executed regardless of whether an exception occurred or not. It's typically used for cleanup actions like closing files or releasing resources.


try:
 # Code that might raise an exception 
 x = int(input("Enter a Number: "))
 result = 10/x
 print("Result: ", result)
except ValueError:
 print("Please enter vaild number.")
except ZeroDivisionError:
 print("Cannot divide vy zero.")
except Exception as e:
 print("An error occurred:", e)

finally: 
 print("This block always executes, regardless of ")

