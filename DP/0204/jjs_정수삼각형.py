# my code: time efficiency
def solution1(triangle):
    answer = [triangle[0][0]]
    for d0, floor in enumerate(triangle[1:]):
        d = d0 + 1
        tmp = []
        for i, number in enumerate(floor):
            if i - 1 == -1:
                tmp.append(number + answer[i])
            elif i == d:
                tmp.append(number + answer[i-1])
            else:
                tmp.append(max(number+answer[i-1], number+answer[i]))
        answer = tmp
                
    return max(answer)

# someone's code: memory efficiency
def solution(triangle):
    for d in range(1, len(triangle)):
        for i in range(d+1):
            if i == 0:
                triangle[d][0] += triangle[d-1][0]
            elif i == d:
                triangle[d][-1] += triangle[d-1][-1]
            else:
                triangle[d][i] += max(triangle[d-1][i-1],
                                      triangle[d-1][i])
    return max(triangle[-1])

# genius' code
def solution(triangle, prev=[]):
    for curr in triangle:
        prev = [max(lp, rp) + xc\
                for lp, rp, xc in zip([0]+prev, prev+[0], curr)]
    return max(prev)