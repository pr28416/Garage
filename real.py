ret = float(input("Enter amount: "))
ret = int(ret * 100)

quarters = 0
dimes = 0
nickels = 0
pennies = 0

quarters += ret // 25
ret %= 25

dimes += ret // 10
ret %= 10

nickels += ret // 5
ret %= 5

pennies += ret

print(f"q: {quarters}, d: {dimes}, n: {nickels}, p: {pennies}")