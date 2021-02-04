def solution(d):
    answer = 0

    for i in range(1, len(d)):
        for j in range(len(d[i])):
            if j == 0:
                d[i][j] = d[i - 1][j] + d[i][j]
            elif j == i:
                d[i][j] = d[i - 1][j - 1] + d[i][j]
            else:
                d[i][j] = max(d[i - 1][j - 1] + d[i][j],
                              d[i - 1][j] + d[i][j])

    answer = max(d[-1])
    return answer