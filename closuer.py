def multiply_outer(n):
    def multiply_inner(x):
        return x * n

    return multiply_inner

val3 = multiply_outer(3)
val5 = multiply_outer(5)
print(val3(9))
print(val5(3))
print("the value of ", val5(val3(2)))