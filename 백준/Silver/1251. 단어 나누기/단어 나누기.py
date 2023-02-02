import sys

words = sys.stdin.readline().rstrip()
answer = []

for i in range(len(words)-2):
    for j in range(i+1, len(words)-1):
        for k in range(j+1, len(words)):
            a = words[:j]
            b = words[j:k]
            c = words[k:]
            answer.append(a[::-1] + b[::-1] + c[::-1])

answer = sorted(answer)

print(answer[0])