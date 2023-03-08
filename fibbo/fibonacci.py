def fibonacci_series(n):
    a=0
    b=1
    series = []
    while a <= n:
        series.append(a)
        a, b = b, a + b
    return series
a=fibonacci_series(10)
print(a)





