# Write code to check if a string represents a valid number (integer or decimal).

s = "123.45"
is_valid_number = True
has_decimal_point = False
if s[0] == '-':
    s = s[1:]

for char in s:
    if char == '.':
        if has_decimal_point:
            is_valid_number = False
            break
        has_decimal_point = True
    elif not char.isdigit():
        is_valid_number = False
        break

print(is_valid_number)
