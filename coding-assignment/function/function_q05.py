# Create a function to find the maximum element in a list.

def find_max(lst):
    max_value = lst[0]
    for num in lst:
        if num > max_value:
            max_value = num
    return max_value

print(find_max([1, 2, 3, 4, 5]))
