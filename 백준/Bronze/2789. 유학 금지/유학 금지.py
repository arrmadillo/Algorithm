import sys

word = sys.stdin.readline().rstrip()
ban = 'CAMBRIDGE'
answer = ''
for i in word:
    if i not in ban:
        answer += i
print(answer)

