def solution(money):
    # 3 1 4 7 2 5
    case1 = [i for i in money]
    case2 = [i for i in money]
    # 첫 번째를 선택하는 경우
    case1[1], case1[-1] = case1[0], 0
    # 첫 번째를 선택하지 않는 경우
    case2[0] = 0

    for i in range(2, len(money)):
        case1[i] = max(case1[i-1], case1[i-2] + case1[i])
        case2[i] = max(case2[i-1], case2[i-2] + case2[i])

    # print(f'case1: {case1}')
    # print(f'case2: {case2}')

    return max(case1[-1], case2[-1])
