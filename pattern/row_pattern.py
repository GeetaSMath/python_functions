# pattern to print row
def num_row(num):
    for i in range(num):
        print("*", end=" ")
    print()
num=int(input("enter user value"))

num_row(num)

def num_col(num_val):
    for i in range(num_val):
        print("*")
    print()
num_val=int(input("enter user value"))
num_col(num_val)
