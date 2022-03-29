n = int(input())

words = []
for _ in range(n):
    words.append(input())
words = list(set(words)) # set으로 중복값 제거

# sort메서드 사용, 안정정렬임을 이용해서 튜플안에 차례대로 조건 삽입
words.sort(key=lambda word: (len(word), word)) # 길이오름차순 -> 사전순
for word in words:
    print(word)