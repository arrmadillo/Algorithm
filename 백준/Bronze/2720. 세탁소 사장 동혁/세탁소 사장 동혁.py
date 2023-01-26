import sys

t = int(sys.stdin.readline())
answer = [0, 0, 0, 0]
money = [25, 10, 5, 1]
for i in range(t):
    change = int(sys.stdin.readline())
    while change != 0:
        for i in range(4):
            answer[i] = change // money[i]
            change = change - (answer[i] * money[i])
    print(*answer)
    answer = [0, 0, 0, 0]