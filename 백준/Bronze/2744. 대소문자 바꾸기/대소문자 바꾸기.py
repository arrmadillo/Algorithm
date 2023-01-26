import sys

t = sys.stdin.readline().rstrip()
answer = []

for i in range(len(t)):
    if t[i].isupper() == True:
        answer.append(t[i].lower())
    else:
        answer.append(t[i].upper())

print(*answer, sep='')









