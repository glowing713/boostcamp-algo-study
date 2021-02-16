N = int(input()) # 지방 수, 3 ~ 10,000
money = list(map(int, input().split()))
M = int(input())

if sum(money) <= M:
    print(max(money))
else:
    money.sort()

    limit = 0
    s = 1
    e = money[-1]
    while s < e:
        mid = (s + e) // 2

        total = 0
        for m in money:
            total += min(m, mid)

        if total <= M:
            s = mid + 1
            limit = mid
        else:
            e = mid
    print(limit)