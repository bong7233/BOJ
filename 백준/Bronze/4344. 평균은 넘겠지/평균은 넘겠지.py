from sys import stdin
input = stdin.readline

n = int(input())

for _ in range(n):
    scores = list(map(float, input().split()))
    count = 0
    students = scores.pop(0)

    for score in scores:
        if score > sum(scores)/students:
            count += 1
    print(f"{round(count/students*100,3):.3f}%")