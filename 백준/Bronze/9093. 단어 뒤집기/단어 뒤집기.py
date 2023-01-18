import sys

t = int(sys.stdin.readline().rstrip())

for i in range(t):
    text = list(input().split())
    for j in range(len(text)):
        text[j] = text[j][::-1]
    print(*text)
    

