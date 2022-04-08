import math


def findOddEvenMax(fibNumber):
    if fibNumber == 1: return "1 0 1"
    n = math.floor(math.log(fibNumber*math.sqrt(5)+0.5)/math.log((1+math.sqrt(5))/2))
    tri = [[0] * i for i in range(1, n+1)]
    for i in range(len(tri)):
        for j in range(len(tri[i])):
            if i == 0 or j == 0 or j == len(tri[i])-1: tri[i][j] = 1
            else: tri[i][j] = tri[i - 1][j - 1] + tri[i - 1][j]
    o, e, l, sc, sd = 0, 0, 0, n//2, n//2-((n+1)%2)
    while sd >= 0:
        if tri[sc][sd] % 2 == 0: e += 1
        else: o += 1
        l = max(tri[sc][sd], l)
        sc += 1; sd -= 1
    return f"{o} {e} {l}"