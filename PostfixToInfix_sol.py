from collections import deque

def postfixToInfix(expr):
    operators = {"^", "*", "/", "%", "+", "-"}
    expr = expr.split(" ")
    stack = deque()
    for i in range(len(expr)):
        symbol = expr[i]
        if symbol in operators:
            a, b = stack.pop(), stack.pop()
            subexpr = f"({b} {symbol} {a})"
            stack.append(subexpr)
        else:  # operand
            stack.append(symbol)
    return stack.pop()