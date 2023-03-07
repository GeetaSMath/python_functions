import random
# Take user input for number of times to flip the coin
num_flips = int(input("Enter the number of times to flip the coin: "))

# Initialize variables for counting heads and tails
num_heads = 0
num_tails = 0

# flip the coin num_flips times and count the number of heads and tails
for i in range(num_flips):
    # if number is less than 0.5 consider as tail else head
    if random.random() < 0.5:
        num_tails += 1
    else:
        num_heads += 1

# Calculate the percentages of heads and tails
pct_heads = (num_heads / num_flips) * 100
pct_tails = (num_tails / num_flips) * 100

# Print the results
print(f"Percentage of heads: {pct_heads:.2f}%")
print(f"Percentage of tails: {pct_tails:.2f}%")

