# Write code to capitalize the first and last letter of each word in a string.

s = "capitalize first and last letters"
result = ""
words = s.split()
for word in words:
    if len(word) > 1:
        word = word[0].upper() + word[1:-1] + word[-1].upper()
    else:
        word = word.upper()
    result += word + " "

print(result.strip())
