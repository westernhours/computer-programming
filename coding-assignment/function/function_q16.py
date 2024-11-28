# Write a function to find the common elements in three lists.

def common_elements(lst1, lst2, lst3):
    return list(set(lst1) & set(lst2) & set(lst3))

print(common_elements([1, 2, 3], [2, 3, 4], [3, 4, 5]))
