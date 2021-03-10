from collections import deque


def bfs(t_x, t_y, height):
    queue = deque()
    # 상 하 좌 우
    mx = [-1, 1, 0, 0]
    my = [0, 0, -1, 1]
    # 시작점
    visited[t_x][t_y] = True
    queue.append((t_x, t_y))

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + mx[k]
            ny = y + my[k]

            if 0 <= nx < n and 0 <= ny < n:
                if area[nx][ny] > height and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))


n = int(input())
area = [list(map(int, input().split())) for _ in range(n)]
min_height = min(map(min, area))  # 최소 물높이
max_height = max(map(max, area))  # 최대 물높이
answer = 1

for h in range(min_height, max_height + 1):
    temp_cnt = 0
    visited = [[False] * n for _ in range(n)]  # 방문체크
    for i in range(n):
        for j in range(n):
            if area[i][j] > h and not visited[i][j]:
                bfs(i, j, h)
                temp_cnt += 1
    answer = max(answer, temp_cnt)

print(answer)
