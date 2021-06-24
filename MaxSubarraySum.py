def maxSubarraySum(arr):
    sums = [0] * (len(arr)+1)
    for i in range(len(arr)):
        sums[i+1] = sums[i] + arr[i]
    largest = [0] * len(sums)
    maxEnd = sums[-1]
    res = False
    for i in range(len(largest)-2, -1, -1):
        largest[i] = max(sums[i+1], maxEnd)
        maxEnd = max(maxEnd, largest[i])
        res = max(res or largest[i]-sums[i], largest[i]-sums[i])
    return res


N = int(input())
ans = maxSubarraySum(list(map(int, input().split(" "))))
print(ans)