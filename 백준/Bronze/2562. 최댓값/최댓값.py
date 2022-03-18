import sys

li = []
for _ in range(9):
    a = int(sys.stdin.readline())
    li.append(a)
    
print(max(li))
print(li.index(max(li)) + 1)