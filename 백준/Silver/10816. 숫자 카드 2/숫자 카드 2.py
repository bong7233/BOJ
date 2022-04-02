import bisect
from sys import stdin

n = int(stdin.readline())
lst1 = list(map(int,stdin.readline().split()))
m = int(stdin.readline())
lst2 = list(map(int,stdin.readline().split()))

lst1.sort()

for i in range(m):
    target = lst2[i]

    start = bisect.bisect_left(lst1, target)
    end = bisect.bisect_right(lst1,target)
    # print('t ', target, 's',start,'e',end)

    if start >= n or lst1[start] != target:
        print(0, end= ' ')
    elif lst1[start] == target and start >= 0:
        print(end-start, end= ' ')