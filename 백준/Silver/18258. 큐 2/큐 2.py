import sys
from collections import deque

q = deque()

n = int(input())

for _ in range(n):
    command = list(sys.stdin.readline().split())

    if command[0] == 'push':  # 함수가 푸시일때
        q.append(command[1])
    elif command[0] == 'pop':
        if len(q) != 0:
            print(q.popleft())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(q))
    elif command[0] == 'empty':
        if len(q) != 0:
            print(0)
        else:
            print(1)
    elif command[0] == 'front':
        if len(q) != 0:
            print(q[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if len(q) != 0:
            print(q[-1])
        else:
            print(-1)