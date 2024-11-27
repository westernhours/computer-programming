# Given a list students = [{"name": "John", "age": 20}, {"name": "Alice", "age": 22}, {"name": "Bob", "age": 20}], group the students by their age.

students = [{"name": "John", "age": 20}, {"name": "Alice", "age": 22}, {"name": "Bob", "age": 20}]
result = {}
for student in students:
    age = student["age"]
    if age not in result:
        result[age] = []
    result[age].append(student)
print(result)
