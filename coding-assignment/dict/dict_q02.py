# Count Character Frequency

s = "hello"
freq = {}
for char in s:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1
print(freq)  # Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}
2. Invert a Dictionary
python
d = {'a': 1, 'b': 2, 'c': 3}
inverted = {v: k for k, v in d.items()}
print(inverted) 
