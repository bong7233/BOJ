import sys

n = int(sys.stdin.readline())

for i in range(n):
    li = list(map(int,str(i)))
    total = i + sum(li)
    if total == n:
        print(i)
        break
    if i == (n-1):
        print(0)