import heapq

INF = 1e9
f, s, g, u, d = map(int, input().split())
distance = [INF]*(f+1)
graph = [[] for _ in range(f+1)]
for i in range(1, f+1):
    if i+u <= f:
        graph[i].append((i+u, 1))
    if i-d >= 1:
        graph[i].append((i-d, 1))

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(s)
if distance[g] == INF:
    print("use the stairs")
else:
    print(distance[g])
