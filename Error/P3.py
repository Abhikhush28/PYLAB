def read_and_process_file(filename):
 try:
  with open(filename, 'r') as file:
   lines = file.readlines()

   # Process data from the file
   numbers = [int(line.strip()) for line in lines]
   total_sum = sum(numbers)
   average = total_sum /len(numbers)
   print('Total Sum: ', total_sum)
   print("Average: ", average)
 except FileNotFoundError:
  print(f"Error: File '{filename}' not found.")
 except PermissionError:
  print("Error: Permission denied to access the file.")
 except ValueError:
  print("Error: Invaild data found  in the file. Ensure all lines contains integers.")
 except ZeroDivisionError:
  print("Error: Division by zero occurred.")
 except Exception as e:
  print("An unexpected  error occurred:", e)
 finally:
  print("Cleanup: Closing file and releasing resources")