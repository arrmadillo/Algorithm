import sys

N, M = map(int, sys.stdin.readline().split())


box = [0 for _ in range(N)]

def shot(start, end, num):
    for i in range(start-1, end):
        box[i] = num

def solution(n, m):
    for _ in range(m):
        start, end, num = map(int, sys.stdin.readline().split())
        shot(start, end, num)
    return box

print(*(solution(N, M)))




