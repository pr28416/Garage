from math import sqrt

def isPrime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n % 2 == 0 or n % 3 == 0: return False
    for k in range(5, int(sqrt(n)+1), 2):
        if n % k == 0:
            return False
    return True

print(isPrime(7))
print(isPrime(11))
print(isPrime(15))
print(isPrime(107))
print(isPrime(127))
print(isPrime(3907))
print(isPrime(3901))

print(*[i for i in range(100) if isPrime(i)])