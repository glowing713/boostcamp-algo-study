import copy

N = int(input())
arr = []
Max = 0
for _ in range(N):
    temp = list(map(int, input().split()))
    Max = max(Max, max(temp))
    arr.append(temp)


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(arr):
    
    
    result = 0
    bi_arr = copy.deepcopy(arr)
    for i in range(N):
        for j in range(N):
            if bi_arr[i][j] == 1:
               
    return result

safe_lands = []
for i in range(Max+1):
    new_arr = []
    for j in range(N):
        new_arr.append([1 if k>i else 0 for k in arr[j]])
    safe_lands.append(safe(new_arr))

print(max(safe_lands))