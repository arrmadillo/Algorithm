import sys

input = sys.stdin.readline()
case = int(input)

answer = [' ' * (case-_) + '*' * _ for _ in range(case,0,-1)]

print(*answer, sep='\n')
