from sys import stdin

n = int(stdin.readline())

for _ in range(n):
    t = int(stdin.readline().strip())
    nums = []
    result = 'YES'
    for _ in range(t):
        nums.append(str(stdin.readline().strip()))

    nums = sorted(nums)

    for i in range(len(nums)-1):
        if nums[i+1][:len(nums[i])] == nums[i]:
            result = 'NO'
            break
    print(result)