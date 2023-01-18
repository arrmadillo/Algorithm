import sys

a = sys.stdin.readline().rstrip()
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
answer = []

for i in alphabet:
    if a.find(i) != -1:
        answer.append(a.find(i))
    else:
        answer.append(-1)

print(*answer)