# Write code to remove all punctuation from a string.

import string
s = "Hello, world! How's it going?"
no_punctuation = ""
for char in s:
    if char not in string.punctuation:
        no_punctuation += char

print(no_punctuation)
