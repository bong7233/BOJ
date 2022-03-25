import heapq
import sys


h = []
n = int(sys.stdin.readline())

for _ in range(n):
    c = int(sys.stdin.readline())
    if c == 0:
        try:
            print(heapq.heappop(h)*-1)
        except:
            print(0)
    else:
        heapq.heappush(h,-c)