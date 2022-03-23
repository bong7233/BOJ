import sys
from collections import deque

n , k = map(int,sys.stdin.readline().split())

q = deque([i for i in range(1,n+1)])

t = 1

print('<', end='')
while len(q) != 1:
    if t % k == 0:
        print(q.popleft(), end=', ')
        t += 1
    else:
        q.append(q.popleft())
        t += 1
print(q.popleft(), end='')
print('>')