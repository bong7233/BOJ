import sys
from collections import deque

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

def bfs(graph, v, visited):
    q = deque([v])
    visited[v] = True
    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


n, e, v = map(int, sys.stdin.readline().split())


adj = [[] for _ in range(n+1)] # 빈 인접리스트 생성

for _ in range(e):   # 간선 수 만큼 반복
    v1, v2 = map(int, sys.stdin.readline().split())
    adj[v1].append(v2)
    adj[v2].append(v1)

for i in range(1, n+1):
    adj[i].sort()

visited = [False]*(n+1)
dfs(adj,v,visited)
print()
visited = [False]*(n+1)
bfs(adj,v,visited)