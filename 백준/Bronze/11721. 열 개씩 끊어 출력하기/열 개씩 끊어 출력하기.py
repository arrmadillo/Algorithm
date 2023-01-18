import sys

t = sys.stdin.readline().rstrip()
for i in range(0, (len(t)//2) + 1):
    print(t[10*i : 10*i + 10])