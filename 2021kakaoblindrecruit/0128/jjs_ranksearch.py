from collections import defaultdict
from itertools import combinations

def solution(info, query):
    record = defaultdict(list)
    for a_info in info:
        a_info_split = a_info.split() # 단 두 번만 사용하더라도 저장해놓는게 빠름
        others = a_info_split[:-1]
        score = int(a_info_split[-1])
        
        record["all"].append(score)
        for n_comb in range(1, 5):
            for combination in combinations(others, n_comb):
                record["".join(combination)].append(score)
    
    for scores in record.values():
        scores.sort()
    
    answer = []
    for q in query:
        q_split = q.split()
        qothers = q_split[::2]
        qscore = int(q_split[-1])
        joined = "".join(qothers).replace("-", "")
        
        scores = record[joined] if joined else record['all']
        start, end = (0, len(scores))
        while start < end:
            mid = (start + end) // 2
            if scores[mid] < qscore:
                start = mid + 1
            else:
                end = mid
        answer.append(len(scores) - start)
    return answer