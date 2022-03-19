def dfs(x, y):
    global count
    if x < 0 or x >= n or y < 0 or y >= n or grid[x][y] != 1:
        return

    grid[x][y] = 0    # 지도에서 0으로 바꾸고
    count += 1        # 집의갯수 + 1

    # 같은작업을 상하좌우로 재귀실행
    dfs(x, y + 1)
    dfs(x, y - 1)
    dfs(x - 1, y)
    dfs(x + 1, y)

n = int(input())
grid = []
for _ in range(n):
    grid.append(list(map(int,input())))

result = []  # 단지별 아파트수
count = 0  # 단지내 아파트수
for x in range(n):
    for y in range(n):
        if grid[x][y] == 1:  # 아파트가있으면 재귀를 실행해서 count 축적
            dfs(x, y)        # 재귀 내부에서는 0을만나도 count 초기화없이 진행
            result.append(count)
            count = 0

print(len(result))
for i in sorted(result):
    print(i)
