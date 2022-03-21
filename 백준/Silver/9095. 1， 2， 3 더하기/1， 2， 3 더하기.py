from sys import stdin

# 백트래킹으로 풀이
def backTracking(num, sum):
    global count
    # 재귀 종결조건(백트래킹 핵심)
    if sum >= n:
        return
    
    # 합에 1,2,3중 하나를 더하고 목표숫자 n과 같으면 count
    sum += num
    if sum == n:
        count +=1
    
    # 첫 num을 0으로두고 1,2,3을 각각 더해주는 세갈래로 재귀
    backTracking(1,sum)
    backTracking(2,sum)
    backTracking(3,sum)


t = int(stdin.readline())

for i in range(t):
    n = int(stdin.readline())
    count = 0
    backTracking(0,0)
    print(count)