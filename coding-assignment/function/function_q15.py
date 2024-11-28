# Write a function to find the second largest element in a list.

def second_largest(lst):
    first, second = float('-inf'), float('-inf')
    for num in lst:
        if num > first:
            first, second = num, first
        elif num > second and num != first:
            second = num
    return second

print(second_largest([1, 2, 3, 4, 5]))
