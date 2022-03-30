import sys

n = int(sys.stdin.readline())

members = []
for _ in range(n):
    members.append(list(sys.stdin.readline().split()))

members.sort(key=lambda member: (int(member[0])))

for member in members:
    print(' '.join(member))