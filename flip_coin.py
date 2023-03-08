import random
# Take user input for number of times to flip the coin
num_flips = int(input("Enter the number of times to flip the coin: "))

NUM_HEADS = 0
NUM_TAILS = 0

# todo by using ternary operator
for i in range(num_flips):
    # if number is less than 0.5 consider as tail else head
    if random.random() < 0.5:
        NUM_TAILS += 1
    else:
        NUM_HEADS += 1

pct_heads = (NUM_HEADS / num_flips) * 100
pct_tails = (NUM_TAILS / num_flips) * 100

# Print the results
print(f"Percentage of heads: {pct_heads:.2f}%")
print(f"Percentage of tails: {pct_tails:.2f}%")



