orig = input()
print(type(orig))
numbers = list(map(int, orig.split(" ")))
print(numbers)
prod = 1
for i in numbers:
    prod *= i
print(prod)
