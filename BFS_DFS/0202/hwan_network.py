def dfs(row, visited, computers, n):
    for j in range(n):
        if computers[row][j] == 1 and not visited[j]:
            visited[j] = 1
            dfs(j, visited, computers, n)


def solution(n, computers):
    answer = 0
    visited = [0 for _ in range(n)]    # 방문체크
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and not visited[j]:  # 연결되어 있지만 아직 지나지 않은 노드일 때,
                answer += 1
                visited[j] = 1
                dfs(j, visited, computers, n)

    return answer
