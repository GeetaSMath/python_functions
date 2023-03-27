# 3 -> "Given a list of words in the singular form,
# return a set of those words in the plural form if they appear more than
# once in the list.
# Examples
# pluralize([""cow"", ""pig"", ""cow"", ""cow""]) ➞ { ""cows"", ""pig"" }
# pluralize([""table"", ""table"", ""table""]) ➞ { ""tables"" }
# pluralize([""chair"", ""pencil"", ""arm""]) ➞ { ""chair"", ""pencil"", ""arm"" }"

def pluralize(lst):
    count_dict = {}
    for word in lst:
        if word not in count_dict:
            count_dict[word] = 1
        else:
            count_dict[word] += 1
    plural_set = set()
    for word, count in count_dict.items():
        if count > 1:
            plural_set.add(word + 's')
        else:
            plural_set.add(word)
    return plural_set


print(pluralize(["cow", "pig", "cow", "cow"]))

print(pluralize(["table", "table", "table"]))
