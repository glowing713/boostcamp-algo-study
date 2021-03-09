"""
# 점화식
0. n == 3이면 셋 중 하나(max값)

1. dp[i] = max(dp[i-1], dp[i-2] + money[i])
- i-th 미포함: dp[i] = dp[i-1]
- i-th 포함: dp[i] = dp[i-2] + money[i]
(초기값 두 개 필요)

# cycle break
1. (n-1)th 미포함 (dp[n-2]까지만 구한다.)
초기값은 dp[0] = money[0], dp[1] = max(money[0], money[1])

2. 0th 미포함
초기값은 dp[0] = 0, dp[1] = money[1]
"""

def solution(money):
    n = len(money) # 3 <= n <= 1e6
    if n == 3:
        return max(money)
    
    # money[n-1] 미포함
    dp = [0] * (n-1)
    dp[0] = money[0]
    dp[1] = max(money[0], money[1])
    for i in range(2, n-1):
        dp[i] = max(dp[i-1], dp[i-2] + money[i])
    answer = dp[n-2]
    
    # money[0] 미포함
    dp = [0] * n
    dp[0] = 0
    dp[1] = money[1]
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + money[i])
        
    if dp[n-1] > answer:
        answer = dp[n-1]
    return answer