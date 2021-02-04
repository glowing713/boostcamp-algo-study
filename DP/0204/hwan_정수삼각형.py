def solution(t):
    max_val = 0
    for i in range(1, len(t)):
        for j in range(len(t[i])):
            # 시작지점
            if j == 0:
                t[i][j] = t[i][j] + t[i-1][j]
            # 끝지점
            elif j == len(t[i])-1:
                t[i][j] = t[i][j] + t[i-1][j-1]
            else:
                t[i][j] += max(t[i-1][j-1], t[i-1][j])
    return max(t[-1])
