import sys

case = int(sys.stdin.readline())

word = set([sys.stdin.readline().rstrip() for i in range(case)])


word = sorted(word) #사전순으로 맞추고
word = sorted(word, key=lambda x: len(x)) #길이순

print(*word, sep='\n')
