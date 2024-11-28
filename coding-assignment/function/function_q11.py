# Create a function to check if a number is a perfect square.

def is_perfect_square(n):
    import math
    return math.isqrt(n) ** 2 == n

print(is_perfect_square(16))
