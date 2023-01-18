import sys

t = list(map(int, sys.stdin.readline().split()))
c = True
while(c):
    for i in range(0, len(t)-1):
        if t[i] > t[i+1]:
            t[i], t[i+1] = t[i+1], t[i]
            print(*t)
        elif t == [1, 2, 3, 4, 5]:
            c = False