def bfs(start, computers, visited):
    que = [start]
    while que:
        now = que.pop(0)
        visited[now] = 1
        for i in range(len(computers)):
            if computers[now][i] == 1 and visited[i] == 0:
                visited[i] = 1
                que.append(i)
              
        

def solution(n, computers):
    answer = 0
    visited = [0]*n
    while 0 in visited:
        idx = visited.index(0)
        bfs(idx, computers, visited)
        answer += 1
    
    return answer