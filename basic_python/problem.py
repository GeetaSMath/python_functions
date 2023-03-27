# In cricket, an over consists of six deliveries a bowler bowls
# from one end. Create a function that takes the number of balls bowled
# by a bowler and calculates the number of overs and balls bowled by him/her.
# Return the value as a float, in the format overs.balls.
# Examples
# total_overs(2400) ➞ 400

# total_overs(164) ➞ 27.2
# 27 overs and 2 balls were bowled by the bowler.

def total_overs():
    ball = int(input("enter the total number of balls"))
    over = ball // 6
    extra_ball = ball % 6

    result = float(f"{over}{extra_ball}")
    get_result = result / 10
    return get_result


overs = total_overs()
print(f"the bowled {overs:.1f} overs.")
# result = total_overs(164)
# result2 =total_overs(2400)
# print(result2)
# print(result)
