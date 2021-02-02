def solution(n, s, a, b, fares):
    INF = 10000000
    answer = INF
    costs = [[INF]*(n+1) for _ in range(n+1)]
    for row in fares:
        start, dest, cost = row
        costs[start][dest] = cost
        costs[dest][start] = cost

    for k in range(1, n+1):
        costs[k][k] = 0
        for i in range(1, n+1):
            for j in range(1, n+1):
                if costs[i][j] > costs[i][k] + costs[k][j]:
                    costs[i][j] = costs[i][k] + costs[k][j]

    for l in range(1, n+1):
        answer = min(answer, costs[s][l] + costs[l][a] + costs[l][b])
    return answer
