from sys import stdin

n, k = map(int,stdin.readline().split())

coins = []
for _ in range(n):
    coins.append(int(stdin.readline()))

count = 0

for coin in coins[::-1]:
    if k//coin > 0 :
        count += (k // coin)
        k %= coin
    if k == 0:
        break
        
print(count)