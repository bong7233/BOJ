import sys

n = int(sys.stdin.readline())
li = []
for _ in range(n):
    x, y = map(int,sys.stdin.readline().split())
    li.append([x,y])

for i in range(len(li)):
    rank = 1
    for j in range(len(li)):
        if li[i][0] < li[j][0] and li[i][1] < li[j][1]:
            rank += 1
    print(rank)