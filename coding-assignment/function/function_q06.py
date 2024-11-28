# Write a function to count the occurrences of a character in a string.

def count_char(s, char):
    count = 0
    for c in s:
        if c == char:
            count += 1
    return count

print(count_char("hello", "l"))
