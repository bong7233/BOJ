from sys import stdin

result = []
for _ in range(10):
    num = int(stdin.readline())
    result.append(num % 42)

print(len(set(result)))