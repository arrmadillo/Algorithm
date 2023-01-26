import sys

t = int(sys.stdin.readline())
answer = [0, 0, 0, 0]

for i in range(t):
    change = int(sys.stdin.readline())
    while change != 0:
        if change >= 25:
            answer[0] = change // 25
            change = change - (answer[0] * 25)
        elif change >= 10:
            answer[1] = change // 10
            change = change - (answer[1] * 10)
        elif change >= 5:
            answer[2] = change // 5
            change = change - (answer[2] * 5)
        else:
            answer[3] = change // 1
            change = change - (answer[3] * 1)
    print(*answer)
    answer = [0, 0, 0, 0]

            

