import sys

N = int(sys.stdin.readline())


def solution(n):
    count = n // 4
    for _ in range(count):
        print('long', end=' ')
    print('int')

solution(N)