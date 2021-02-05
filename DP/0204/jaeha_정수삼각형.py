def solution(triangle):
    answer = 0
    for i in range(1, len(triangle)):
        for j in range(i+1):
            if j == 0:
                up_left = 0
            else:
                up_left = triangle[i-1][j-1]
            if j == i:
                up_right = 0
            else:
                up_right = triangle[i-1][j]
            triangle[i][j] = triangle[i][j]+ max(up_left, up_right)
    answer = max(triangle[-1])
    return answer