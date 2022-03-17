n = int(input())

target = n
count = 0

while True:
    count += 1
    a = n // 10
    b = n % 10
    c = (a + b) % 10

    n = (10 * b) + c
    if n == target:
        break

print(count)