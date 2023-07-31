import sys

a, b = map(int, sys.stdin.readline().split())

def solution(a, b):
    return 2 * b - a

print(solution(a, b))