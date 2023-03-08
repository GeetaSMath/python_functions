from functools import lru_cache
# a function that returns a function or takes another function as an argument

# lru_cache will store the result



@lru_cache(None)
def fibonacci(num: int) -> int:

	# checking if num is less than 0, it will return none
	if num < 0:
		print("Incorrect input")
		return

	# check if num between 1, 0,  it will return num
	elif num < 2:
		return num

	# return the fibonacci of num - 1 & num - 2
	return fibonacci(num - 1) + fibonacci(num - 2)


# Driver Program
print(fibonacci(3))
