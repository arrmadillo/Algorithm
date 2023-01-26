import sys

t = int(sys.stdin.readline())
want = list(map(int, sys.stdin.readline().split()))
seat = []
count = 0

for i in want:
    if i not in seat:
        seat.append(i)
    else:
        count += 1
print(count)


