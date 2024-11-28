# Reverse the order of keys in a dictionary.

d = {'a': 1, 'b': 2, 'c': 3}
reversed_d = {k: d[k] for k in reversed(list(d.keys()))}
print(reversed_d)
