# Write a Python program to display calendar.

import calendar

year = int(input("Year : "))
month = int(input("Month : "))
display = calendar.month(year, month)
print(display)
