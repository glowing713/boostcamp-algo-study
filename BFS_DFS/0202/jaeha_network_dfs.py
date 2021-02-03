def solution(n, computers):
    answer = 0
    visited = [0]*n
    while 0 in visited:
        start = visited.index(0)
        stack = [start]
        while stack:
            now = stack.pop()
            visited[now] = 1
            for i in range(len(computers)):
                if computers[now][i] == 1 and visited[i] == 0:
                    stack.append(i)
        answer += 1
    return answer