from collections import deque
def solution(numbers, target):
    answer = 0
    que = deque([(0,0)])
    while que:
        value , idx = que.popleft()
        if idx == len(numbers):
            if value == target:
                answer+=1
        else:
            que.append((value+numbers[idx], idx+1))
            que.append((value-numbers[idx], idx+1))
    return answer   