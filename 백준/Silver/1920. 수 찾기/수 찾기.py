import collections

n = input()
list_a = list(map(int,input().split()))
m = input()
list_b = list(map(int,input().split()))

hash_a = collections.Counter(list_a)

for char in list_b:
    if hash_a[char] >= 1:
        print(1)
    else:
        print(0)
