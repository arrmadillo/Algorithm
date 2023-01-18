import sys

word = sys.stdin.readline().rstrip()
ban = 'CAMBRIDGE'
print(*[i for i in word if i not in ban], sep='')