# Write code to count the number of words in a string that start with a vowel.

s = "A big apple fell on an elephant"
vowels = "aeiouAEIOU"
words = s.split()
count = 0
for word in words:
    if word[0] in vowels:
        count += 1

print(count)
