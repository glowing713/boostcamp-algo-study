def solution(m, n, puddles):
    maps = [[0]*(m+1) for _ in range(n+1)]
    dp = [[0]*(m+1) for _ in range(n+1)]
    # 물 체크
    for pud in puddles:
        maps[pud[1]][pud[0]] = -1

    dp[1][0] = 1  # 시작지점은 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if maps[i][j] == -1:
                dp[i][j] = 0
            else:
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000007
    return dp[n][m]
