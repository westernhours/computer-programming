# Write a program to filter tuples where the sum of elements is greater than a specified value.

tuples_list = [(1, 2), (3, 4), (0, 0), (10, -5)]
threshold = 3
filtered_tuples = [t for t in tuples_list if sum(t) > threshold]
print(filtered_tuples)
