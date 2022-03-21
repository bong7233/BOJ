import sys

n = input()

scores = list(map(float, sys.stdin.readline().split()))

max_score = max(scores)

for i in range(len(scores)):
    scores[i] = (scores[i]/max_score) * 100

result = (sum(scores))/float(n)

print(result)