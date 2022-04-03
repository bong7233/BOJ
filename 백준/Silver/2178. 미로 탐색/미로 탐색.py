from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())

maze = []
for _ in range(n):
    maze.append(list(map(int,stdin.readline().strip())))

def bfs(x,y):
    dx = [-1,0,0,1]
    dy = [0,1,-1,0]

    dq = deque()
    dq.append((x,y))
    while dq:
        x, y = dq.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or ny<0 or nx>=n or ny>=m or maze[nx][ny] == 0:
                continue

            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                dq.append((nx,ny))

    return maze[n-1][m-1]

print(bfs(0,0))

