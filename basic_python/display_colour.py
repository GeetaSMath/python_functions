# 3. Write a Python program to display the first and last colors from the following list.
# color_list = ["Red","Green","White" ,"Black"]

def display_first_and_last_colors(color_lst):
    first_color = color_lst[0]
    last_color = color_lst[-1]
    print("First color:", first_color)
    print("Last color:", last_color)


color_list = ["Red", "Green", "White", "Black"]
display_first_and_last_colors(color_list)
