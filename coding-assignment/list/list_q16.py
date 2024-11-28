# Rearrange the list so that all even numbers come before odd numbers:

my_list = [1, 2, 3, 4, 5, 6, 7, 8]
even = [x for x in my_list if x % 2 == 0]
odd = [x for x in my_list if x % 2 != 0]
rearranged_list = even + odd
print(rearranged_list)
