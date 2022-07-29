from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)


def reverse_string(str):
    stack = Stack()
    rev = ""
    for letter in str:
        stack.push(letter)

    while not stack.is_empty():
        rev += stack.pop()

    return rev


print(reverse_string("We will conquere COVID-19"))


def is_balanced(str):
    stack = Stack()

    parentheses = {"(": ")", "{": "}", "[": "]"}

    for element in str:
        if element in parentheses.keys():
            stack.push(element)

        if element in parentheses.values():
            if stack.is_empty():
                return False

            if parentheses[stack.peek()] == element:
                stack.pop()
            else:
                return False

    return True


def is_match(ch1, ch2):
    match_dict = {")": "(", "]": "[", "}": "{"}

    return match_dict[ch1] == ch2


def is_balanced_alt(str):
    stack = Stack()

    for ch in str:
        if ch == "(" or ch == "{" or ch == "[":
            stack.push(ch)

        if ch == ")" or ch == "}" or ch == "]":
            if stack.size() == 0:
                return False
            if not is_match(ch, stack.pop()):
                return False

    return stack.size() == 0


print(is_balanced_alt("({a+b})"))
print(is_balanced_alt("))((a+b}{"))
print(is_balanced_alt("((a+b))"))
print(is_balanced_alt("))"))
print(is_balanced_alt("[a+b]*(x+2y)*{gg+kk}"))
