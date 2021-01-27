from itertools import combinations
from collections import Counter

def solution(orders, course):
    for i in range(len(orders)):
        orders[i] = ''.join(sorted(orders[i]))
    
    candidates = {}
    max_nums = {}
    
    for n in course:
        candidates[n] = []
        max_nums[n] = -1
    
    for order in orders:
        for n in course:
            if len(order) >= n:
                candidates[n] += combinations(order, n)
    
    for n in course:
        candidates[n] = Counter(candidates[n])
        if candidates[n]:
            max_num = max(list(candidates[n].values()))
            if max_num >= 2:
                max_nums[n] = max_num
    
    answer = []
    for n in course:
        answer += [''.join(k) for k, v in candidates[n].items() if v == max_nums[n]]
    
    return sorted(answer)
