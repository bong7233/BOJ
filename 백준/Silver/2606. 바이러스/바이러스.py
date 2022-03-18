n = int(input())  # 컴퓨터수
m = int(input())  # 연결 수

# n x n 의 0으로 채워진 행렬 생성( 인접행렬로 변환시키기 위한 default )
graph = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    # 인접행렬에서 서로 연결되있는 부분은 0->1로 변환
    graph[a][b] = graph[b][a] = 1

# 감염한 컴퓨터를 index순서대로 나타내는 0리스트 생성, 감염시 1로 변경
visited = [0]*(n+1)

# dfs 구현
def dfs(v):    
    visited[v] = 1  # 감염된 컴퓨터는 1로 변경
    for i in range(n+1):
        if graph[i][v] == 1 and visited[i] == 0: # 감염된 컴퓨터인데 visited에 적용되지않은경우
            dfs(i) # 그 감염된 컴퓨터를 기준으로 다시 dfs 재귀

# 1번컴퓨터 바이러스감염            
dfs(1)

# 1번컴퓨터를 제외한 감염된 컴퓨터수
print(sum(visited)-1)

