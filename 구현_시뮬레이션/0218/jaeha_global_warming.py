import copy

r,c = map(int, input().split())
arr = []
for _ in range(r):
    arr.append(list(input()))
new_arr = copy.deepcopy(arr)
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
for y in range(r):
    for x in range(c):
        cnt = 0
        for i in range(4):
            if x+dx[i] >= 0 and x+dx[i] < c and y+dy[i] >=0 and y+dy[i] < r:
                if arr[y+dy[i]][x+dx[i]] == '.':
                    cnt += 1
            else:
                cnt += 1
        if cnt >= 3:
            new_arr[y][x] = '.' 
min_x, min_y, max_x, max_y = c, r, 0, 0
for y in range(r):
    for x in range(c):
        if new_arr[y][x] == 'X':
            min_x = min(min_x, x)
            min_y = min(min_y, y)
            max_x = max(max_x, x)
            max_y = max(max_y, y)

for y in range(min_y, max_y+1):
    print(''.join(new_arr[y][min_x:max_x+1]))

print(new_arr)