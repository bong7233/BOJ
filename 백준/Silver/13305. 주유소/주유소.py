from sys import stdin

n = int(input())

dis = list(map(int,stdin.readline().split()))
oils = list(map(int,stdin.readline().split()))

total = dis[0]*oils[0]
cur_oil = oils[0]

for i in range(1, len(dis)):
    if cur_oil > oils[i]:
        cur_oil = oils[i]
        total += cur_oil*dis[i]
    else:
        total += cur_oil*dis[i]

print(total)