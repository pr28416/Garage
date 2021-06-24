def maxSubarraySum(arr):
    sums = [0] * (len(arr) + 1)
    for i in range(len(arr)):
        sums[i+1] = sums[i] + arr[i]
    maxEnd = sums[-1]
    res = False
    for i in range(len(sums)-2, -1, -1):
        maxEnd = max(maxEnd, sums[i+1])
        res = max(res or maxEnd-sums[i], maxEnd-sums[i])
    return res

import MaxSubarraySum_Checker