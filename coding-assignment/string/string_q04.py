#  Write a program to check if a given string containing only parentheses '(', ')', '{', '}', '[' and ']' is valid. A string is valid if open brackets are closed in the correct order.

def is_valid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)

    return not stack

s = "()[]{}"
print(is_valid(s))
