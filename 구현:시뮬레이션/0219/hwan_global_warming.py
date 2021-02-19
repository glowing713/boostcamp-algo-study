import sys
import copy

r = sys.stdin.readline


# 바다에 인접한 면의 수
def findOceans(i: int, j: int, maps: list) -> int:
    oceans = 0
    row, col = len(maps)-1, len(maps[0])-1
    # 좌우상하
    mx, my = [0, 0, -1, 1], [-1, 1, 0, 0]
    for d in range(4):
        nx, ny = i + mx[d], j + my[d]  # 좌우상하 방향 위치
        if nx < 0 or nx > row or ny < 0 or ny > col or maps[nx][ny] == '.':
            oceans += 1
    return oceans


def solve(row: int, col: int, maps: list) -> list:
    cp_maps = copy.deepcopy(maps)  # 수정할 지도
    for i in range(row):
        for j in range(col):
            if maps[i][j] == 'X':
                if findOceans(i, j, maps) >= 3:
                    cp_maps[i][j] = '.'

    start_i, end_i, start_j, end_j = 0, 0, col-1, 0

    for i in range(row):
        if 'X' in cp_maps[i]:
            start_i = i
            break
    for i in range(row-1, -1, -1):
        if 'X' in cp_maps[i]:
            end_i = i
            break

    for i in range(start_i,  end_i+1):
        tmp = [i for i, value in enumerate(cp_maps[i]) if value == 'X']
        if not tmp:
            continue
        min_tmp = tmp[0]
        max_tmp = tmp[-1]
        start_j = min(start_j, min_tmp)
        end_j = max(end_j, max_tmp)

    for i in range(start_i, end_i+1):
        print(''.join(cp_maps[i][start_j:end_j+1]))


row, col = map(int, r().split())
maps = [list(r().rstrip()) for _ in range(row)]  # 원본 지도

solve(row, col, maps)
