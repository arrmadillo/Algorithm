import sys

case = int(sys.stdin.readline())
cup = [1, 2, 3]

for _ in range(case):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    cup[a-1], cup[b-1] = cup[b-1], cup[a-1]

print(cup.index(1) + 1)