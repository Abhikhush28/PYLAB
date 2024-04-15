# [9:36 AM] N Murugadoss (Unverified)
def get_integer_input(prompt):

    try:

        value = int(input(prompt))

        return value

    except ValueError:

        print("Error: Invalid input, input a valid integer.")
 
n = get_integer_input("Input an integer: ")

print("Input value:", n)
