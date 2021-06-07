# def isPal(n):
#     return str(n)[::-1] == str(n)

# c = 0
# m = 0
# for i in range(100, 1000):
#     if isPal(i):
#         c += 1
#         m += i
# print(m / c)

# def test(x1, x2, x3, x4, x5):
#     return 1 if (x1*x2*x3+x2*x3*x4+x3*x4*x5+x4*x5*x1+x5*x1*x2) % 3 == 0 else 0

# nums = [1, 2, 3, 4, 5]
# used = [False] * 5
# total = 0
# x=0
# for a in range(5):
#     used[a] = True
#     for b in range(5):
#         if used[b]: continue
#         used[b] = True
#         for c in range(5):
#             if used[c]: continue
#             used[c] = True
#             for d in range(5):
#                 if used[d]: continue
#                 used[d] = True
#                 for e in range(5):
#                     if used[e]: continue
#                     used[e] = True
#                     x+= 1
#                     print(a+1, b+1, c+1, d+1, e+1)
#                     total += test(a+1, b+1, c+1, d+1, e+1)
#                     used[e] = False
#                 used[d] = False
#             used[c] = False
#         used[b] = False
#     used[a] = False

# print(total)
# print(x)

# Problem 9

from math import gcd
c = 0
for i in range(1, 31):
    for j in range(1, 31):
        if gcd(2**i+1, 2**j-1) != 1:
            print(i, j)
            c+=1
print(c)

# Problem 13
# n = 1
# while (2**n+5**n-n) % 1000 != 0:
#     n+=1
# print(n)

# Problem 15
# from math import sqrt
# def f(n):
#     if int(sqrt(n)) == sqrt(n): return int(sqrt(n))
#     else:
#         return 1+f(n+1)
# def g(n):
#     if int(sqrt(n)) == sqrt(n): return int(sqrt(n))
#     else:
#         return 2+g(n+2)
# n = 1
# while f(n)/g(n) != 4/7:
#     n += 1
# print(n)

# Define printSubsets() function
# subsets = []

# def printSubsets(lst, toggles=None, i=0):
#     global subsets
#     if toggles == None:
#         toggles = [0] * len(lst)

#     if i >= len(lst):
#         subsets.append({lst[i] for i in range(len(lst)) if toggles[i] == 1})

#     else:
#         toggles[i] = 0
#         printSubsets(lst, toggles, i+1)
#         toggles[i] = 1
#         printSubsets(lst, toggles, i+1)


# # Test function
# printSubsets([1, 2, 3, 4, 5])
# # print(subsets)
# # print(len(subsets))

# c = 0
# for a in subsets:
#     for b in subsets:
#         if len(a) * len(b) == len(a & b) * len(a | b):
#             c += 1
# print(c)

# Problem 11

# totalSum = 0
# def ck(x, y):
#     return x % 6 == 0 and y % 7 == 0

# for a in range(10, 97):
#     b, c, d = a+1, a+2, a+3
#     combs = [ck(a, b),ck(a, c),ck(a, d),ck(b, a), ck(b, c), ck(b, d),ck(c, a),ck(c, b),ck(c, d),ck(d, a),ck(d, b),ck(d, c)]
#     if ck(a, b) or ck(a, c) or ck(a, d) or ck(b, a) or ck(b, c) or ck(b, d) or ck(c, a) or ck(c, b) or ck(c, d) or ck(d, a) or ck(d, b) or ck(d, c):
#         print(a, b, c, d)
#         print(combs)
#         totalSum += d
# print(totalSum)