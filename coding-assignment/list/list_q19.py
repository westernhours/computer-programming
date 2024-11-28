# Calculate the product of all elements in a list except itself.

nums = [1, 2, 3, 4]
result = []
for i in range(len(nums)):
    prod = 1
    for j in range(len(nums)):
        if i != j:
            prod *= nums[j]
    result.append(prod)
print(result)
