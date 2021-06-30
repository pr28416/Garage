def subarraySums1(n, x, arr):
    sums = [0] * (n+1)
    for i in range(len(arr)):
        sums[i+1] = sums[i]+arr[i]
    lo, up = n-1, n
    count = 0
    while not (lo == 0 and up == 0):
        # print(lo, up)
        if sums[up]-sums[lo] == x:
            count += 1
            lo = max(0, lo-1)
            up = max(0, up-1)
        elif sums[up]-sums[lo] < x:
            if lo == 0: break
            lo -= 1
        else:
            if up == 0: break
            up -= 1
    return count

print(subarraySums1(*map(int, input().split(" ")), list(map(int, input().split(" ")))))