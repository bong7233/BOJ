h, m = map(int, input().split())

t = int(input())

if m+t < 60:
    print(h, m+t)
else:
    print(((h + ((m+t)//60))%24) , (m+t)%60)