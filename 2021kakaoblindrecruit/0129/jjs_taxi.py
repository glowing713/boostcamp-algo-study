from collections import defaultdict, deque
from heapq import heappush, heappop

def get_fare(dest, graph):
    fares = {node: float("inf") for node in graph}
    fares[dest] = 0
    
    q = []
    heappush(q, (fares[dest], dest)) # push/pop by x[0] = total fare
    while q:
        total, curr = heappop(q) # pop the minimum total
        for adj, w in graph[curr]:
            new_total = total + w
            if new_total < fares[adj]: # update
                heappush(q, (new_total, adj))
                fares[adj] = new_total
    
    return fares

def solution(n, s, a, b, fares):
    graph = defaultdict(list)
    for c, d, f in fares:
        graph[c].append((d, f))
        graph[d].append((c, f))
    
    # fare to home(a/b) from a certain node
    # use dict for search
    fare_to_a = get_fare(a, graph)
    fare_to_b = get_fare(b, graph)
    
    # 2. find the minimum fare; answer
    answer = float("inf")
    q = deque()
    q.append((s, 0))
    visit = dict()
    visit[s] = 0 # do not visit again unless it is better
    while q:
        dep, total = q.popleft()
        if dep == a: # a's home is on the way to b's home
            total += fare_to_b[dep]
            answer = min(answer, total) # not decided yet
            continue # but this way is over decidedly
        if dep == b:
            total += fare_to_a[dep]
            answer = min(answer, total)
            continue
        
        # maybe, time to go separate ways
        answer = min(answer, total + fare_to_a[dep] + fare_to_b[dep])
        # this way is not over
        for dest, w in graph[dep]:
            new_total = total + w
            if (dest in visit) and (new_total >= visit[dest]):
                continue # visited once, and not a better way
            # otherwise,
            q.append((dest, new_total))
            visit[dest] = new_total

    return answer

# Floyd-Warshall: simple and fast to code
def solution1(n, s, a, b, fares):
    m = n + 1
    dist = [[float("inf")] * m for _ in range(m)]
    for i in range(1, m): # nodes are natual numbers
        dist[i][i] = 0    # no move cost = 0
    for c, d, f in fares: # otherwise, f
        dist[c][d] = f
        dist[d][c] = f

    # Floyd-Warshall Algorithm
    # : shortest path for all i-j pairs dist[i][j]
    for k in range(1, m): # stopover
        for i in range(1, m):
            for j in range(1, m):
                bypass = dist[i][k] + dist[k][j]
                if bypass < dist[i][j]:
                    dist[i][j] = bypass
    
    # find the minimum dist
    answer = float("inf")
    for k in range(1, m): # intersection
        total = dist[s][k] + dist[k][a] + dist[k][b]
        if total < answer:
            answer = total

    return answer