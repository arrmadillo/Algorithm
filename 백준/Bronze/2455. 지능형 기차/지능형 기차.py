import sys

answer = []
result = 0

for _ in range(4):
    out_num, in_num = map(int, sys.stdin.readline().rstrip().split())
    result = result - out_num + in_num
    answer.append(result)
print(max(answer))