# Sort a dictionary by keys.

d = {'b': 1, 'a': 2, 'c': 3}
sorted_d = {k: d[k] for k in sorted(d)}
print(sorted_d)
