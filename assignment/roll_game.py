# Repeat this for three rounds.
# But if you roll DOUBLES, your score is instantly wiped to 0 and your game ends immediately!
#
# Create a function that takes in a list of tuples as input, and return John's score after his game has ended.
#
# Examples
# dice_game([(1, 2), (3, 4), (5, 6)]) ➞ 21
#
# dice_game([(1, 1), (5, 6), (6, 4)]) ➞ 0
#
# # dice_game([(4, 5), (4, 5),

def play_dic(val):
    a = 0
    for vals in val:
        if val[0] == vals[1]:
            return 0
        a += sum(vals)
    return a
print(play_dic([(4, 5), (4, 5), (4, 5)]))
print(play_dic(([(1, 1), (5, 6), (6, 4)])))
print(play_dic(([(1, 2), (3, 4), (5, 6)])))
