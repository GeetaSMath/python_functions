# Create a function that returns the majority vote in a list.
# A majority vote is an element that occurs > N/2 times in a list (where N is the length of the list).
# Examples
# majority_vote(["A", "A", "B"]) ➞ "A"
# majority_vote(["A", "A", "A", "B", "C", "A"]) ➞ "A"
# majority_vote(["A", "B", "B", "A", "C", "C"]) ➞ None

def majority_vote(lst):
    n = len(lst)
    for item in set(lst):
        if lst.count(item) > n/2:
            return item
    return None
print(majority_vote(["A", "A", "B"]))
print(majority_vote(["A", "A", "A", "B", "C", "C"]))
print(majority_vote(["A", "A", "A", "B", "C", "A"]))