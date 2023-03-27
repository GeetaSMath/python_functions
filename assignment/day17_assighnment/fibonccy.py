# In mathematics, the Fibonacci numbers, commonly denoted Fn,
# form a sequence, called the Fibonacci sequence,
# such that each number is the sum of the two preceding ones, starting from 0 and 1:
# F0 = 0, F1 = 1,
# and
# Fn = F(n-1) F(n-2)
# for n > 1
# The beginning of the sequence is thus:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
# The function fib_fast(num) returns the fibonacci number Fn, of the given num as an argument.
# Examples
# fib_fast(5) ➞ 5
# fib_fast(10) ➞ 55
# fib_fast(20) ➞ 6765

def fib_fast():
    num = int(input("enter the index of fibonacci"))
    fib = [0, 1]
    for i in range(2, num + 1):
        fib.append(fib[i - 1] + fib[i - 2])

    return fib[num]

print(fib_fast())
#print(fib_fast(5))
#print(fib_fast(10))
#print(fib_fast(20))