# Write a function that takes coordinates of two points on
# a two-dimensional plane and returns the length of the line segment connecting those two points.
#
# Examples
# line_length([15, 7], [22, 11]) ➞ 8.06
# line_length([0, 0], [0, 0]) ➞ 0
# line_length([0, 0], [1, 1]) ➞ 1.41
#
# Note:
# use operator for exponent value

def line_length(points1, points2):
    x1, x2 = points1
    y1, y2 = points2
    len = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return round(len, 2)


print(line_length([15, 7], [22, 11]))
print(line_length([0, 0], [0, 0]))
print(line_length([0, 0], [1, 1]))
