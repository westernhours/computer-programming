# Write a program to find the tuple with the minimum sum of elements from a list of tuples.

tuples_list = [(1, 2), (3, 4), (0, 0), (10, -5)]
min_tuple = min(tuples_list, key=sum)
print(min_tuple) 
