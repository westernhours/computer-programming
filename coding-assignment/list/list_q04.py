# List Sorting
# Given a list students = [{"name": "John", "age": 20}, {"name": "Alice", "age": 22}, {"name": "Bob", "age": 21}], sort the list by age in descending order.

students = [{"name": "John", "age": 20}, {"name": "Alice", "age": 22}, {"name": "Bob", "age": 21}]
students.sort(key=lambda x: x["age"], reverse=True)
print(students)
