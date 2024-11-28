# Generate a dictionary with list values.

d = {}
for i in range(5):
    d[i] = list(range(i, i+3))
print(d)
