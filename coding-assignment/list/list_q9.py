# Reverse a list in place without using the built-in reverse method.

lst = [1, 2, 3, 4, 5]
left, right = 0, len(lst) - 1
while left < right:
    lst[left], lst[right] = lst[right], lst[left]
    left += 1
    right -= 1
print(lst)
