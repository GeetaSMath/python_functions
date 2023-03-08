def check_even_odd(num):
    num =f"{num} is even" if num % 2 == 0 else f"{num}is odd"
    print(num)

if __name__ == '__main__':

    check_even_odd(5)
    check_even_odd(10)