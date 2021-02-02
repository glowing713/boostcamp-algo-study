from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    for c in course:
        cnt = []
        for o in orders:
            for s in map(lambda x: ''.join(x), combinations(sorted(o), c)):
                cnt.append(s)
        cnt = Counter(cnt).most_common()
        if cnt:
            max_cnt = cnt[0][1]
            for menu, m_cnt in cnt:
                if m_cnt == max_cnt and m_cnt > 1:
                    answer.append(menu)
    return sorted(answer)
