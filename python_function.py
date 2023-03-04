# python function
# why we need function , to reduced code re-usability
# Syntax def function_name()
# Display Message using function
def wish_me():
    print("Hello Python")
    print("Have good future")
    wish_me()


# create function and pass arguments
# create function
def item_list(name):
    print("item is", name)
    item_list("Laptop")


# add two numbers
def add_numbers(n1, n2):
    result = n1 + n2
    print("The sum is", result)
    number1 = 5
    number2 = 7
    add_numbers(number1, number2)


# Closure is function object that remembered value in enclosing scopes if they are not present
def multiply_outer(n):
    def multiply_inner(x):
        return x * n

    return multiply_inner


val3 = multiply_outer(3)
val5 = multiply_outer(5)
print(val3(9))
print(val5(3))
print("the value of ", val5(val3(2)))


# example for closure
def outer_func(msg):
    message = msg

    def inner_func():
        print(message)

    return inner_func


hi_func = outer_func('hi')
bye_func = outer_func('bye')
hi_func()
bye_func()


# decorator's  function to modify the behaviour of function or class
# the functions accepts other function as an arguments is called higher order function
# fun decoration
def start_end_doc(func):
    def wrapper():
        print('start')
        func()
        print('end')

    return wrapper


@start_end_doc
def get_name():
    print('alexa')


# get_name = start_end_doc(get_name)
get_name()


# when func has args to pass
def start_end_doc(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result

    return wrapper


@start_end_doc
def get_num5(x):
    return x + 5


result = get_num5(5)
print(result)


# class  based decoration
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f'this is executed {self.num_calls} times')
        return self.func(*args, **kwargs)


@CountCalls
def say_hello():
    print('hello')


say_hello()
say_hello()


# higher order fun
# higher order function is fun that accept fun as args
def loud(text):
    return text.upper()


def quite(text):
    return text.lower()


def hello(func):
    text = func("Hello")
    print(text)


hello(loud)
hello(quite)

# lambda function to sort list
a = [[1, 4], [2, 6], [8, 9]]
a.sort(key=lambda x: x[1])
print(a)


# CALLER AND CALEE FUNCTION
# EXA
def subtract(a, b):
    print(a - b)


subtract(5, 8)


def multiply(x, y):
    print(x * y)


multiply(2, 4)


# find simpleInterest problem
def simpleInterest(price, time, rate):
    return price * time * rate / 100


x = simpleInterest(1000, 2, 5)
print('simple interest is', x)
