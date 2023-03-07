# Take input from the user
year = int(input("Enter a 4-digit year: "))

# Check if the year is a leap year or not
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")
