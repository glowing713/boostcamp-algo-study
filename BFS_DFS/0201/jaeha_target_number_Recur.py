
def DFS(numbers, target, idx):
    if idx == len(numbers):
        if target == 0:
            return 1
        return 0
    else:
        return DFS(numbers, target+numbers[idx], idx+1) + DFS(numbers, target-numbers[idx], idx+1)
        
def solution(numbers, target):
    answer = DFS(numbers, target, 0)
    return answer