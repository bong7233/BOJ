import heapq
from sys import stdin
INF = int(1e9)

v, e = map(int,stdin.readline().split())
start_node = int(input())

graph = [[] for _ in range(v+1)]
for _ in range(e):
    s, e, d = map(int,stdin.readline().split())
    graph[s].append((e,d))

distance = [INF] * (v+1)

def dj(graph, start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for next_node, cur_dist in graph[now]:
             total_dist = dist + cur_dist
             if distance[next_node] > total_dist:
                 distance[next_node] = total_dist
                 heapq.heappush(q, (total_dist, next_node))

dj(graph,start_node)

for d in distance[1:]:
    if d == 1e9:
        print('INF')
    else:
        print(d)
