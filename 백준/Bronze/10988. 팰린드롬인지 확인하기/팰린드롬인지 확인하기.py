import sys

word = sys.stdin.readline().rstrip()

size = len(word) // 2

if word[:size] == word[-1:-size-1:-1]:
    print(1)
else:
    print(0)

