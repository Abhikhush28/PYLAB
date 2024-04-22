# Python program to demonstrate date class

# import  the date class 
from datetime import date, datetime

my_date = date(1996, 12, 31)
today = date.today()
print('Date passed as argument is ', my_date)
print("Today Date: ", today)
print("Current year: ", today.year)
print("Current Month: ", today.month)
print("Current Day: ", today.day)


date_time = datetime.fromtimestamp(2454634356)
print("Datetime from timestamp: ", date_time)

