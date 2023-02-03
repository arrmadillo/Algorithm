import sys

words = sys.stdin.readline().rstrip()

answer = []
#완전탐색
for i in range(1, len(words)-1):
    for j in range(i+1, len(words)):
        answer.append(words[:i][::-1] + words[i:j][::-1] + words[j:][::-1]) #뒤집어 넣기
            
answer = sorted(answer) #사전순

print(answer[0])