numbers = set(range(1, 10000))
non_self = set()

for num in numbers :
    for n in str(num):
        num += int(n)
    non_self.add(num)
    
self_nums = numbers - non_self

for self_num in sorted(self_nums):
    print(self_num)