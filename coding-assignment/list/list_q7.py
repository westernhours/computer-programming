#Find the largest and smallest number in a list.

lst = [3, 1, 4, 1, 5, 9, 2, 6, 5]
largest = lst[0]
smallest = lst[0]
for num in lst:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num
print("Largest:", largest)
print("Smallest:", smallest)
