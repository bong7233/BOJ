from sys import stdin
input = stdin.readline

n = int(input())


result = 0
count = 0

for _ in range(n):
    ox = input()
    for i in range(len(ox)):
        if ox[i] == 'O':
            count += 1
            result += count
        else:
            count = 0
    print(result)
    result = 0