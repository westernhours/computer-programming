# Check if all values in a dictionary are greater than a certain number.

d = {'a': 5, 'b': 10, 'c': 3}
all_greater_than_2 = all(value > 2 for value in d.values())
print(all_greater_than_2)
