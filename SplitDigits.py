def splitDigitsPositive(num):
    digits = []
    while num > 0:
        digits.append(num % 10)
        num //= 10
    return digits[::-1]

def splitDigitsNonnegative(num):
    if num == 0: return [0]
    digits = []
    while num > 0:
        digits.append(num % 10)
        num //= 10
    return digits[::-1]

def splitDigitsAny(num):
    if num == 0: return [0]
    isNeg = num < 0
    num = abs(num)
    digits = []
    while num > 0:
        digits.append(num % 10)
        num //= 10
    if isNeg: digits[-1] *= -1
    return digits[::-1]

print(splitDigitsAny(12345))
print(splitDigitsAny(420230))
print(splitDigitsAny(0))
print(splitDigitsAny(-500967))
print(splitDigitsAny((-1384)))