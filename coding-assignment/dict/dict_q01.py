# Write a dictionary comprehension that creates a dictionary of squares for even numbers between 1 and 10.

squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(squares)
