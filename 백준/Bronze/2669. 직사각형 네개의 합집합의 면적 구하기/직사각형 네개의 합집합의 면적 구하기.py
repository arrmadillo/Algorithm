import sys

temp = [[0]*100 for _ in range(100)]
count = 0

for _ in range(4):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    x1, y1, x2, y2 = x1, y1, x2-1, y2-1
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            
            if temp[i][j] == 1:
                continue
            else:
                temp[i][j] = 1
                count += 1

print(count)
            
