import sys

t = int(sys.stdin.readline())

for _ in range(t):
    score = list(map(int, sys.stdin.readline().split())) 
    new_score = score[:]
    max_num = max(new_score)
    min_num = min(new_score)
    new_score.remove(max_num)
    new_score.remove(min_num)

    new_score = sorted(new_score)
    if new_score[-1] - new_score[0] >= 4:
        print('KIN')
    else:
        print(sum(new_score))
    # for score in new_score:
    #     print('점수:',score)
    #     if max_num - score >= 4 or score - min_num > 4:
    #         print('KIN')
    #         # print(max_num)
    #         break
    # else:
    #     print(sum(new_score))







