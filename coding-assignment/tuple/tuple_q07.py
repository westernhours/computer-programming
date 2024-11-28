# Write a program to find all tuples that have all positive elements.

tuples_list = [(1, 2), (-3, 4), (0, 0), (10, -5), (2, 3)]
positive_tuples = [t for t in tuples_list if all(x > 0 for x in t)]
print(positive_tuples)
