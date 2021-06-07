from collections import deque

def prefixToInfix(expr):
    operators = {"^", "*", "/", "%", "+", "-"}
    expr = expr.split(" ")
    stack = deque()
    # right to left
    for i in range(len(expr)-1, -1, -1):
        # get symbol
        symbol = expr[i]
        if symbol in operators: # symbol is operator
            # get two most recent operands and make
            # them into a subexpression
            subexpr = f"({stack.pop()} {symbol} {stack.pop()})"
            # add the subexpression back to the stack
            stack.append(subexpr)
        else: # operand
            # add it to the stack
            stack.append(symbol)
    return stack.pop()


print(prefixToInfix("* + A B - C D"))