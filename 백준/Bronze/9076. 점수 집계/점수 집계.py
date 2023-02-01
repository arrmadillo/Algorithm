import sys

t = int(sys.stdin.readline())

for _ in range(t):
    score = list(map(int, sys.stdin.readline().split())) 
    score = sorted(score)
    max_num = score[-1]
    min_num = score[0]
    new_score = score[1:-1]
    
    if new_score[-1] - new_score[0] >= 4:
        print('KIN')
    else:
        print(sum(new_score))








