import sys

t = int(sys.stdin.readline().rstrip())
grade = list(map(int,sys.stdin.readline().split()))
best_grade = max(grade)
average = 0

for i in grade:
    average += i / best_grade * 100
print(average/len(grade))
    





