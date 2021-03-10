import sys

r = sys.stdin.readline

n = int(r())
hp_loss = list(map(int, r().split()))
pleasure = list(map(int, r().split()))
dp = [[0]*101 for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(100):
        if j < hp_loss[i-1]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-hp_loss[i-1]] + pleasure[i-1])

print(dp[n][99])
