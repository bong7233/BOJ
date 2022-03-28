from sys import stdin

n = int(stdin.readline())
students = []
for _ in range(n):
    student = list(stdin.readline().split())
    students.append(student)

sort_n = sorted(students, key=lambda student: student[0])
sort_m = sorted(sort_n, key=lambda student: int(student[3]), reverse=True)
sort_e = sorted(sort_m, key=lambda student: int(student[2]))
sort_k = sorted(sort_e, key=lambda student: int(student[1]), reverse=True)

for student in sort_k:
    print(student[0])
