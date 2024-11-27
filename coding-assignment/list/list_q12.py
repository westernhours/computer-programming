# Find the median of a list of numbers.

lst = [3, 5, 1, 4, 2]
lst.sort()
n = len(lst)
median = (lst[n // 2] if n % 2 != 0 else (lst[n // 2 - 1] + lst[n // 2]) / 2)
print("Median:", median)
