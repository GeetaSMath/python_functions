# 6. Write a Python program to calculate number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days
# date module in python

import datetime


def days_between_dates(date1, date2):
    # Convert the date tuples to date objects
    date1_obj = datetime.date(*date1)
    date2_obj = datetime.date(*date2)
    delta = date2_obj - date1_obj
    return delta.days


date1 = (2014, 7, 2)
date2 = (2014, 7, 11)
days = days_between_dates(date1, date2)
print("Number of days between", datetime.date(*date1), "and", datetime.date(*date2), "is", days)
