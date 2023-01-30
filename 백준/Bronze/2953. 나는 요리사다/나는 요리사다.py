import sys

result = []

for i in range(1, 6):
    t = sum(list(map(int, sys.stdin.readline().split())))
    result.append((t,i))

result = sorted(result, reverse=True)
print(result[0][-1], result[0][0])