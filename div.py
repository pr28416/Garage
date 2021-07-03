# def primeFactors(n):
#     factors = []
#     while n % 2 == 0:
#         factors.append(2)
#         n //= 2
#     for i in range(3, min(int(n**0.5)+1, n+1), 2):
#         while n % i == 0:
#             factors.append(i)
#             n //= i
#     if n > 1: factors.append(n)
#     return factors


# print(primeFactors(196))

from math import gcd

lcm = lambda x, y: x*y//gcd(x,y)

r = 1
for i in range(2, 21):
    r = lcm(r, i)
print(r)