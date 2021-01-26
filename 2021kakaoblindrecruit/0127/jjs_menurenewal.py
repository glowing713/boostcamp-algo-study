from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    menu_candidates = defaultdict(int)
    for combi_size in course:
        for order in orders:
            ordered_combis = combinations(order, combi_size)
            ordered_combis = list(map("".join, map(sorted, ordered_combis)))
            for ordered_combi in ordered_combis:
                menu_candidates[ordered_combi] += 1
    
    order_count_by_combi_size = defaultdict(int)
    menu_candidate_by_combi_size = defaultdict(list)
    for menu_candidate, order_count in menu_candidates.items():
        if order_count >= 2:
            combi_size = len(menu_candidate)
            if order_count > order_count_by_combi_size[combi_size]:
                order_count_by_combi_size[combi_size] = order_count
                menu_candidate_by_combi_size[combi_size] = [menu_candidate]
            elif order_count == order_count_by_combi_size[combi_size]:
                menu_candidate_by_combi_size[combi_size].append(menu_candidate)
    
    answer = []
    for combi_size in course:
        answer.extend(menu_candidate_by_combi_size[combi_size])
    answer.sort()
    return answer