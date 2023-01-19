import sys

t = int(sys.stdin.readline())

for i in range(t):
    result = sys.stdin.readline().rstrip()
    bonus = 0
    score = 0
    for i in result:
        if i == 'O':
            if bonus == 0:
                bonus = 1
            score += bonus
            bonus += 1
        else:
            bonus = 0
    print(score)



    





