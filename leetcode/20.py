
def isValid(s):
    stack = []
    parantheses = {
        '(':')',
        '{':'}',
        '[':']'
    }
    for bracket in s:
        if bracket in parantheses:
            stack.append(bracket)
        elif len(stack) == 0 or bracket != parantheses[stack.pop()]:
            return False
    return len(stack) == 0

s = "({[]})"
print(isValid(s))