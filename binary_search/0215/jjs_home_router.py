import sys
# input
N, C = map(int, sys.stdin.readline().split())
xs = list(map(int, sys.stdin.readlines()))
xs.sort()

# 이분 탐색
ans = 1
lo = 1
hi = (xs[-1] - xs[0])//(C - 1) + 1 # 한 개는 xs[0]에
while lo < hi:
    mid = (lo + hi) // 2
    
    prev_c = xs[0]
    cnt = 1
    for x in xs:
        if x - prev_c >= mid:
            prev_c = x
            cnt += 1
    
    if cnt >= C:
        ans = mid
        lo = mid + 1
    else:
        hi = mid
print(ans)