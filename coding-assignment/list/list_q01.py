#  List Comprehension with Multiple Conditions
# Given a list numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9], create a new list that contains only the numbers that are greater than 3 and less than 7.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = [x for x in numbers if x > 3 and x < 7]
print(result)
