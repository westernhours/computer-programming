# Write code to find all permutations of a given string.

s = "abc"
permutations = []

def permute(prefix, remaining):
    if len(remaining) == 0:
        permutations.append(prefix)
    for i in range(len(remaining)):
        permute(prefix + remaining[i], remaining[:i] + remaining[i+1:])

permute("", s)
print(permutations)
