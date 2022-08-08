def isValid(s: str) -> bool:
    stack = []
    legend = {")": "(", "}": "{", "]": "["}

    for i in s:
        if i in legend:
            if stack and legend[i] == stack[-1]:
                stack.pop()
            else:
                return False
        else:
            stack.append(i)

    if len(stack) > 0:
        return False

    return True


if __name__ == "__main__":
    tests = ["]", "()", "()[]{}", "(]"]

    for elements in tests:
        print(isValid(elements))
