# Convert a string to an integer without using int().

s = "12345"
result = 0
for char in s:
    result = result * 10 + (ord(char) - ord('0'))
print(result)
