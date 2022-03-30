import heapq
from sys import stdin

n = int(input())
cardList = []
result = 0

for i in range(n):
    heapq.heappush(cardList, int(stdin.readline()))

while len(cardList) > 1:
    n1 = heapq.heappop(cardList)
    n2 = heapq.heappop(cardList)
    total = n1 + n2
    result += total
    heapq.heappush(cardList,total)

print(result)