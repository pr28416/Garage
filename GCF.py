from math import gcd

def gcf(a,b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

lcm = lambda a,b: a*b//gcf(a,b)

x, y = 434377154304, 1962948231

print(gcd(x,y))
print(gcf(x,y))