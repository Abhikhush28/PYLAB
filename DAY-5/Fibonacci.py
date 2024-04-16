# [10:23 AM] N Murugadoss (Unverified)
# START Procedure Fibonacci(n)   declare f0, f1, fib, loop        set f0 to 0   set f1 to 1       display f0, f1        for loop ← 1 to n           fib ← f0 + f1          f0 ← f1       f1 ← fib       display fib    end for END



# [10:24 AM] N Murugadoss (Unverified)
#Python code for fibonacci Series
def fibonacci(n):
 if n == 0:
  return 0
 elif n == 1:
  return 1
 else:
  return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Enter the Number: "))
for i in range(n):
 print(fibonacci(n))