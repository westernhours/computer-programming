# Rearrange the list such that negative numbers appear before positive numbers:

my_list = [12, -7, -5, 3, -6, 2, -1, 11]
rearranged_list = [x for x in my_list if x < 0] + [x for x in my_list if x >= 0]
print(rearranged_list)
