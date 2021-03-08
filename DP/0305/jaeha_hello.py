N = int(input())
L = [0] + list(map(int, input().split()))
J = [0] + list(map(int, input().split()))
dp = [[0]*100 for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(1, 100):
        dp[i][j] = dp[i-1][j]
        if j-L[i] >= 0 and dp[i-1][j-L[i]] + J[i] > dp[i][j]:
            dp[i][j] = dp[i-1][j-L[i]] + J[i]
print(dp[N][99])

