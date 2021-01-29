def solution(n, s, a, b, fares):
    INF = int(1e9)
    answer = int(1e9)
    graph = [[INF]*(n+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j :
                graph[i][j] = 0
    
    for c, d, f in fares:
        graph[c][d] = f
        graph[d][c] = f
        
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
    
    for k in range(1, n+1):
        answer = min(answer, graph[s][k]+graph[k][a]+graph[k][b])
     
    return answer