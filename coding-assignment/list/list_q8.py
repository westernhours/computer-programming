# Group elements of a list based on a given criteria (even and odd numbers).

lst = [1, 2, 3, 4, 5, 6]
evens = [num for num in lst if num % 2 == 0]
odds = [num for num in lst if num % 2 != 0]
print("Evens:", evens)
print("Odds:", odds)
