import sys

N, M = map(int, sys.stdin.readline().split())


box = [_ for _ in range(1, N+1)]


def change(i, j):
    temp = box[i-1]
    box[i-1] = box[j-1]
    box[j-1] = temp

def solution(n, m):
    for _ in range(m):
        i, j  = map(int, sys.stdin.readline().split())
        if i == j:
            continue
        change(i, j)
    return box

print(*(solution(N, M)))




