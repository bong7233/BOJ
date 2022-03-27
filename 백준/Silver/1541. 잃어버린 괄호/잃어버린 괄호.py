arr = input().split('-')  # 입력값을 -기준으로 나눈다
# - 기준으로 나눈 값들중 맨앞값을 제외한 나머지를 모두빼주면 최소값이 된다

cnt = 0
for i in arr[0].split('+'): # 값들을 각각 +값으로 다시 나눠서 숫자만 남김
    cnt += int(i)           # 첫번째 값은 더해준다
for j in arr[1:]:           # 이후값들은 전부 빼준다
    for n in j.split('+'):
        cnt -= int(n)
print(cnt)


