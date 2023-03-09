# "Given a list of integers representing the color of each sock, determine how many pairs of
# socks with matching colors there are.
# For example, there are 7 socks with colors [1, 2, 1, 2, 1, 3, 2].
# There is one pair of color 1 and one of color 2.
# There are three odd socks left, one of each color. The number of pairs is 2.
#
# Create a function that returns an integer representing the number of matching pairs of socks that are available.

def socks_pair(socks):
    sock_count ={}
    pair_count = 0
    for sock in socks:
        if sock in sock_count:
            sock_count[sock] +=1
        else:
            sock_count[sock] =1
    for count in sock_count.values():
        pair_count += count // 2
    return pair_count
print(socks_pair(([10, 20, 20, 10, 10, 30, 50, 10, 20])))



