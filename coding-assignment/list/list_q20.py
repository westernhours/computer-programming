# Convert an integer to Roman numerals.

num = 1987
value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
roman = ""
for i in range(len(value)):
    while num >= value[i]:
        roman += symbols[i]
        num -= value[i]
print(roman)
