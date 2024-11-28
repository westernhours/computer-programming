# Write code to check if one string is a rotation of another string.

s1 = "waterbottle"
s2 = "erbottlewat"
is_rotation = False

if len(s1) == len(s2) and s1 in s2 + s2:
    is_rotation = True

print(is_rotation)
