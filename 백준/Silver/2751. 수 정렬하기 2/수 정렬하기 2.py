import heapq
import sys

n = int(sys.stdin.readline())

hq = []
for _ in range(n):
    heapq.heappush(hq, int(sys.stdin.readline()))

for _ in range(len(hq)):
    print(heapq.heappop(hq))