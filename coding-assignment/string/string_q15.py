# Write code to remove all instances of a given character from a string.

s = "hello world"
char_to_remove = 'o'
result = ""
for char in s:
    if char != char_to_remove:
        result += char

print(result)
