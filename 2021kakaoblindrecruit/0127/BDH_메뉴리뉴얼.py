from itertools import combinations


def tuple_to_str(tp_input):
    # input: ('a', 'b', 'c'), output: 'abc'
    return ''.join(tp_input)


def sort_str(str_input):
    # input: 'cba', output: 'abc'
    str_list = list(str_input)
    str_list.sort()

    return ''.join(str_list)


def solution(orders, course):
    # 2 <= len(orders) <= 20
    # 1 <= len(course) <= 10, course : 오름차순 정렬되어 있음

    answer = []

    for num_menu in course:
        comb_count = {}  # key: menu조합, value: menu조합 count

        for order in orders:
            for menus in combinations(order, num_menu):
                comb = sort_str(tuple_to_str(menus))

                if comb not in comb_count:
                    comb_count[comb] = 1
                else:
                    comb_count[comb] += 1
        # print(comb_count)
        comb_count = [(k, v) for k, v in sorted(comb_count.items(), key=lambda x: -x[1]) if v >= 2]
        print(comb_count)

        if comb_count:
            max_count = comb_count[0][1]

            for menu, count in comb_count:
                if count == max_count:
                    answer.append(menu)
                else:
                    break

    answer.sort()

    return answer