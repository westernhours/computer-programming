# Write code to find and replace a substring in a given string.

s = "Hello, World!"
old_substr = "World"
new_substr = "Universe"
result = ""
i = 0
while i < len(s):
    if s[i:i+len(old_substr)] == old_substr:
        result += new_substr
        i += len(old_substr)
    else:
        result += s[i]
        i += 1

print(result)
