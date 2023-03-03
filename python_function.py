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
    print("item is", name)    # passing arguments
# print item_list which is passed arguments
item_list("Laptop")

# add two numbers
def add_numbers(n1, n2):
    result = n1 + n2
    print("The sum is", result)

number1 = 5
number2 = 7
add_numbers(number1, number2)



#CALLER AND CALEE FUNCTION
#EXA
def subtract(a, b):
    print (a-b)
subtract(5,8)

def multiply(x, y):
    print(x*y)
multiply(2,4)



def simpleInterest(price,time,rate):
    return price*time*rate/100

x= simpleInterest(1000,2,5)
print('simple insterest is', x)






