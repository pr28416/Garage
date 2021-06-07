from collections import deque

def prefixToInfix(expr):
    operators = {'^', '*', '/', '%', '+', '-'}
    expr = expr.split(" ")
    stack = deque()

    for i in range(len(expr)-1, -1, -1):
        symbol = expr[i]
        if symbol in operators:
            subexpr = f"({stack.pop()} {symbol} {stack.pop()})"
            stack.append(subexpr)
        else:
            stack.append(symbol)

    return stack.pop()

prefix = "* + A B - 124 D"
infix = prefixToInfix(prefix)
print(infix)