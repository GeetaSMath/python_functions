import datetime
from datetime import date

d = date(2022, 12, 25)
print(d)

# get current date
current_date = datetime.date.today()

print(current_date)

# get the current date and time
now = datetime.datetime.now()

print(now)

d = datetime.date(2022, 12, 25)
print(d)

timestamp = date.fromtimestamp(1326244364)
print("Date =", timestamp)