import sys
sys.setrecursionlimit(10**6)

### DFS 구현
def solution(grid):
    def dfs(i,j):
        if i<0 or j<0 or i>=n or j>=m or grid[i][j] != 1:
            return
        grid[i][j] = 0
        dfs(i, j+1)
        dfs(i, j-1)
        dfs(i+1, j)
        dfs(i-1, j)

    count = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                dfs(i, j)
                count += 1
    return count

# 문제풀이 시작
t = int(input())

# 배추밭 2차원배열 생성
for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    grid = [[0 for col in range(m)] for row in range(n)]
    for _ in range(k):
        y, x = map(int,sys.stdin.readline().split())
        grid[x][y] = 1

    print(solution(grid))