# Find all pairs of elements in the list whose sum is equal to a specified number (e.g., 10):

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_sum = 10
pairs = [(my_list[i], my_list[j]) for i in range(len(my_list)) for j in range(i + 1, len(my_list)) if my_list[i] + my_list[j] == target_sum]
print(pairs)
