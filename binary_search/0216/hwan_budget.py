import sys

r = sys.stdin.readline

def binary_search(requests: list, budget: int) -> int:
    result = 0
    left = 1
    right = max(requests)
    while left <= right:
        mid = (left + right) // 2
        total_sum = sum(mid if req >= mid else req for req in requests)
        if total_sum <= budget:
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    return result

_, bud_requests, total_bud = r(), list(map(int, r().split())), int(r())
print(binary_search(bud_requests, total_bud))
