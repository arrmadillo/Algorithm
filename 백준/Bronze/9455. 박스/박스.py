import sys

case = int(sys.stdin.readline().rstrip())

for _ in range(case): #케이스
    lines, num = map(int, sys.stdin.readline().rstrip().split())# 줄, 개수
    
    temp = [list(map(int, sys.stdin.readline().rstrip().split())) for i in range(lines)]
    answer = 0

    for col in range(num):
        count = 0 #움직여야할 거리
        for row in range(lines-1, -1, -1):
            if temp[row][col] == 1:
                    answer += count
            else:
                count +=1
    print(answer) 



