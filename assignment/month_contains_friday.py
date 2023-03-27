# "Given the month and year as numbers, return whether that month contains a Friday 13th.
# Examples
# has_friday_13(3, 2020) ➞ True
# has_friday_13(10, 2017) ➞ True
# has_friday_13(1, 1985) ➞ False"

import datetime

def day_friday(year, month):
    find_date =datetime.datetime(year, month, 13)
    return find_date.strftime("%A")

