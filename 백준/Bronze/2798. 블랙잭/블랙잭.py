from itertools import combinations
import sys

n , m = map(int, sys.stdin.readline().split())
cards = list(map(int,sys.stdin.readline().split()))

temp = 0
for card in combinations(cards,3):
    total = sum(card)
    if temp < total <= m:
        temp = total

print(temp)