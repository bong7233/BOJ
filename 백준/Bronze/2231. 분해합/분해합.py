import sys

n = int(sys.stdin.readline())

for i in range(n):
    total = i
    for j in str(i):
        total += int(j)
    if total == n:
        print(i)
        break
    if i == (n-1):
        print(0)