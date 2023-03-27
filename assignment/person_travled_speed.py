# "If a person traveled up a hill for 18mins at 20mph
# and then traveled back down the same path at 60mph
# then their average speed traveled was 30mph.
# Write a function that returns the average speed traveled given
# an uphill time, uphill rate and a downhill rate. Uphill time is given in minutes.
# Return the rate as an integer (mph). No rounding is necessary.
# Examples
# ave_spd(18, 20, 60) ➞ 30
# ave_spd(30, 10, 30) ➞ 15
# ave_spd(30, 8, 24) ➞ 12"

def travel_average_speed(uphill_rate, down_hill_rate, uphill_time):
    distance = (uphill_rate /60) * uphill_time * 2
    time_count = distance /uphill_rate + distance /down_hill_rate
    avg_speed = distance /time_count
    return int(avg_speed)
print(travel_average_speed(18, 20, 60))