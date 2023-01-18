import sys

t = int(sys.stdin.readline().rstrip())

for i in range(t):
    num, word = map(str, sys.stdin.readline().split())
    num = int(num)
    answer = ''
    for i in word:
        answer += i * num
    print(answer)

