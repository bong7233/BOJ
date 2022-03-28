from sys import stdin

n = int(stdin.readline())
students = []
for _ in range(n):
    student = list(stdin.readline().split())
    students.append(student)

# 이런식의 코드도 가능하지만 왜 역순으로 작동하는지는 
# students.sort(key=lambda student: student[0])                       # 이름 오름차순
# students.sort(key=lambda student: int(student[3]), reverse=True)    # 수학 내림차순
# students.sort(key=lambda student: int(student[2]))                  # 영어 오름차순
# students.sort(key=lambda student: int(student[1]), reverse=True)    # 국어 내림차순

# 튜플을 활용하여 원하는 정렬기준을 순서대로 입력 (국어,영어,수학,이름) 
# 오름차순은 음수처리로 간단하게 해결
students.sort(key=lambda student: (-int(student[1]), int(student[2]), -int(student[3]), student[0]))

for student in students:
    print(student[0])