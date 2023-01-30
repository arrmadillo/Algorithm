import sys

temp = [[0]*100 for _ in range(101)]
count = 0

for _ in range(4):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    x1, y1, x2, y2 = x1, y1, x2-1, y2-1 #좌표가 아닌 넓이를 표현하기 위하여
    for i in range(x1, x2+1):           # 넓이 1 사각형은 왼쪽아래, 오른쪽 위 좌표가 x,y 1씩 차이
        for j in range(y1, y2+1):
            
            if temp[i][j] == 1:
                continue
            else:
                temp[i][j] = 1
                count += 1

print(count)