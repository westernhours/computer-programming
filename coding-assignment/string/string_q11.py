# Write code to check if two strings are anagrams of each other.

s1 = "listen"
s2 = "silent"
sorted_s1 = "".join(sorted(s1))
sorted_s2 = "".join(sorted(s2))

if sorted_s1 == sorted_s2:
    print("Anagrams")
else:
    print("Not Anagrams")
