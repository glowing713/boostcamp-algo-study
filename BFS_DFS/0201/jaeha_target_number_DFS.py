def solution(numbers, target):
    answer = 0
    stack = [(0,0)]
    while stack:
        value, idx = stack.pop()
        if idx == len(numbers):
            if value == target:
                answer += 1
        else:
            stack.append((value+numbers[idx], idx+1))
            stack.append((value-numbers[idx], idx+1))
    return answer