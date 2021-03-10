def solution(m, n, puddles):
    answer = 0
    road = [[0]*(n+1) for _ in range(m+1)]
    for x in range(1, m+1):
        for y in range(1, n+1):
            if [x, y] in puddles:
                continue
            if x == 1 and y == 1:
                road[x][y] = 1
            else:
                road[x][y] = road[x-1][y] + road[x][y-1]
    answer = road[m][n] % 1000000007
    return answer