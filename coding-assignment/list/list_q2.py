#List Merging with Custom Logic
#Given two lists list1 = [1, 2, 3] and list2 = [4, 5, 6], merge them into a single list, but only include elements that are not present in both lists.

list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = [x for x in list1 + list2 if (x in list1) ^ (x in list2)]
print(result)
