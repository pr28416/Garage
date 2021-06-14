def numberOfSubsets(N):
    if N*(N+1)%4 != 0: return 0
    dp = [0] * (N*(N+1)//2+1)
    dp[0] = 1
    for newNum in range(1, N+1):
        for totalSum in range(newNum*(newNum+1)//2, newNum-1, -1):
            dp[totalSum] += dp[totalSum-newNum]
    return dp[N*(N+1)//4]//2

print(numberOfSubsets(7))