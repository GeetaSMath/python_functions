# 5. Write a Python program to print the calendar of a given month and year.
# Note : Use 'calendar' module.

import calendar

def print_calendar(year, month):
    cal = calendar.month(year, month)
    print("Calendar of", calendar.month_name[month], year)
    print(cal)

print_calendar(2023, 3)
