# Create a function that takes a function func and counts its arguments.
# Examining a function's bytecode using __code__ is disabled.
#
# Examples
# num_args(lambda: "") ➞ 0
# num_args(lambda x: "") ➞ 1
# num_args(lambda x, y: "") ➞ 2
import inspect


def num_args(func):
    return len(inspect.signature(func).parameters)


print(num_args(lambda: ""))
print(num_args(lambda x: ""))
print(num_args(lambda x, y: ""))
