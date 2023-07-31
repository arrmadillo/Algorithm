import sys

a, b = map(int, sys.stdin.readline().split())

def solution(a, b):
    return a * b - 1

print(solution(a, b))