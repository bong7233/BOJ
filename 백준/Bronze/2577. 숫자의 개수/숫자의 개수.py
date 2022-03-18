import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())

total = str(a * b * c)  # 반복하기위해 str로 변환


dic = {}
for i in range(10):
    dic[str(i)] = 0    # 0~9를 키로 0을 값으로가지는 딕셔너리 생성

for char in total:
    if char in dic.keys():  # total의 숫자 갯수만큼 딕셔너리에 저장
        dic[char] += 1

result = list(dic.values()) # 딕셔너리.valies 하면 자동으로 sort
while result:
    print(result.pop(0))    # 앞에서부터 print
