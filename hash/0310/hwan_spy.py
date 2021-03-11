from collections import defaultdict


def solution(clothes):
    ddict = defaultdict(list)
    total_case = 1  # 조합으로 가능한 수
    for name, tag in clothes:
        ddict[tag].append(name)
    for c_list in ddict.values():
        total_case *= (len(c_list) + 1)
    return total_case - 1
