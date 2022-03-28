from sys import stdin

n = int(stdin.readline())

li = list(map(int,stdin.readline().split()))
li.sort()

if len(li) == 1:
    print(li[0])
elif len(li) % 2 == 0:
    print(li[(len(li)//2)-1])
else:
    print(li[(len(li) // 2)])