# "Create a function to perform basic arithmetic operations" \
# " that includes addition, subtraction, multiplication and division on a string number" \
# " (e.g. ""12 + 24"" or ""23 - 21"" or ""12 // 12"" or ""12 * 21"").
#
# Here, we have 1 followed by a space, operator followed by another space and
# 2. For the challenge, we are going to have only two numbers between 1 valid operator.
# The return value should be a number.
#
# eval() is not allowed. In case of division, whenever the second number equals ""0"" return
# Todo switch
def artmetic_operation(val: str) -> float:
    number1, operator, number2 = val.split()
    number1, number2 = float(number1), float(number2)
    if operator == '+':
        return number1 + number2
    elif operator == '-':
        return number1 - number2
    elif operator == '*':
        return number1 * number2
    elif operator == '//':
        if number2 == 0:
            return -1
        return number1 // number2
        return


print(artmetic_operation("12 + 24"))
