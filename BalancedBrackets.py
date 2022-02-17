from collections import deque

def isBalanced(str):
    stack = deque()
    brackets = {'(':')', '[': ']', '{': '}'}
    for char in str:
        if char in brackets:
            stack.append(char)
        else:
            if len(stack) == 0 or char != brackets[stack.pop()]:
                return False
    return len(stack) == 0

string = "([(){}]()){[]})"

print(isBalanced(string))