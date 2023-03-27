try:
    x = int(input("enter user num"))
    y = int(input("enter user num"))
    result = x / y
    print(result)
except ZeroDivisionError:
    print("denominator cant divide by zero")

print("done....")
