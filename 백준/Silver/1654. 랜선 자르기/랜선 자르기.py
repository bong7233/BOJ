from sys import stdin

k, n = map(int, stdin.readline().split())

lans = [int(stdin.readline().strip()) for _ in range(k)]

lans.sort()

low = 1
high = lans[-1]

while low <= high:
    cnt = 0
    mid = (high + low) // 2
    for lan in lans:
        cnt += lan//mid

    if cnt >= n:
        low = mid + 1
    else:
        high = mid - 1

print(high)