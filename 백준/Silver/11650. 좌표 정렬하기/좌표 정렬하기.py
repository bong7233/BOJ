from sys import stdin

n = int(stdin.readline())
dots = []
for _ in range(n):
    dot = list(map(int,stdin.readline().split()))
    dots.append(dot)

dots.sort(key= lambda dot: (dot[0], dot[1]))

for dot in dots:
    print(' '.join(map(str,dot)))