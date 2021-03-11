from collections import defaultdict
import math

def solution(clothes):
    cnt_by_category = defaultdict(lambda: 1) # start from 1(no use)
    for name, category in clothes:
        cnt_by_category[category] += 1
        
    return math.prod(cnt_by_category.values()) - 1 # exclude no use all