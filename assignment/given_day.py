# "Create a function which returns how many Friday 13ths there are in a given year.
#
# Examples
# how_unlucky(2020) ➞ 2
#
# how_unlucky(2026) ➞ 3
#
# how_unlucky(2016) ➞ 1"

import datetime


def unlucky(year):
    count = 0
    for month in range(1, 13):
        get_day = datetime.datetime(year, month, 13)
        if get_day.weekday() == 4:
            count += 1
    return count


print(unlucky(2020))
print(unlucky(2026))
print(unlucky(2016))
