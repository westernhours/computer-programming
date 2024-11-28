# Write a program to convert a tuple of strings to a tuple of integers.

str_tuple = ('1', '2', '3', '4')
int_tuple = tuple(map(int, str_tuple))
print(int_tuple)
