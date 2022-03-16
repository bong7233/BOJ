from sys import stdin

N, M = map(int, stdin.readline().split())

page_pw = {}
for _ in range(N):
    page, pw = stdin.readline().split()
    page_pw[page] = pw

for _ in range(M):
    print(page_pw[stdin.readline().rstrip()])