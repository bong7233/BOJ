n = int(input())
cnt = n

for _ in range(n):
    word = input()
    stack = []
    for char in word:
        if char in stack and char != stack[-1]:
            cnt -= 1
            break
        else:
            stack.append(char)

print(cnt)