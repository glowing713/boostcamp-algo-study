############
# DFS 풀이
############

# answer = 0


# def dfs(sum, index, numbers, target):
#     global answer
#     size = len(numbers)
#     if index == size:   # 끝까지 확인 다 함
#         if sum == target:
#             answer += 1
#         return
#     dfs(sum + numbers[index], index + 1, numbers, target)
#     dfs(sum - numbers[index], index + 1, numbers, target)


# def solution(numbers, target):
#     global answer
#     dfs(0, 0, numbers, target)
#     return answer

#########################
# cartasian product 풀이
#########################

from itertools import product


def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    print(list(map(sum, product(*l))).count(target))
    s = list(map(sum, product(*l)))
    return s.count(target)
