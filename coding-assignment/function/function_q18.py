# Write a function to find the first missing positive integer in a list.

def first_missing_positive(lst):
    lst = [x for x in lst if x > 0]
    lst.sort()
    missing = 1
    for num in lst:
        if num == missing:
            missing += 1
    return missing

print(first_missing_positive([3, 4, -1, 1]))
