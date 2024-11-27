#  List Filtering
#Given a list numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9], create a new list that contains only the even numbers.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)
