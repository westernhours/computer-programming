# Find all triplets in the list that sum up to a given value (e.g., 0):

my_list = [-1, 0, 1, 2, -1, -4]
triplets = []
my_list.sort()
for i in range(len(my_list) - 2):
    if i > 0 and my_list[i] == my_list[i - 1]:
        continue
    l, r = i + 1, len(my_list) - 1
    while l < r:
        s = my_list[i] + my_list[l] + my_list[r]
        if s == 0:
            triplets.append((my_list[i], my_list[l], my_list[r]))
            while l < r and my_list[l] == my_list[l + 1]:
                l += 1
            while l < r and my_list[r] == my_list[r - 1]:
                r -= 1
            l += 1
            r -= 1
        elif s < 0:
            l += 1
        else:
            r -= 1
print(triplets)
