from itertools import combinations
def solution(orders, course):
    answer = []
    for i in course: # 2, 3, 4
        order_dic = {}
        for order in orders: #
            order_comb = list(combinations(order, i))
            for j in order_comb:
                j = sorted(j)
                order = "".join(j)
                if order not in order_dic:
                    order_dic[order] = 1
                else:
                    order_dic[order] += 1
        
        order_dic = sorted(order_dic.items(), key= lambda x: x[1], reverse=True)
        print(order_dic)
        maxv =0
        for k, v in order_dic:
            if v <= 1:
                break
            elif v < maxv:
                break
            else:
                answer.append(k)
                maxv = v
    answer.sort()
    return answer