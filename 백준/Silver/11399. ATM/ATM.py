from sys import stdin

n = int(stdin.readline().strip())
times = list(map(int, stdin.readline().split()))

times.sort()

total = 0
for i in range(n):
    total += sum(times[:i+1])

print(total)