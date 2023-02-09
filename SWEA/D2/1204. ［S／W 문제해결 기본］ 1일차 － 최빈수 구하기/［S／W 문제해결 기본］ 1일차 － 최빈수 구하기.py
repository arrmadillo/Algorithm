t = int(input())
from pprint import pprint
for i in range(1, t+1):
    case_num = int(input())
    socore = list(map(int,input().split()))
    dic_socore = {}
    for j in range(len(socore)):
        try:
            dic_socore[socore[j]] += 1
        except:
            dic_socore[socore[j]] = 1
    answer = sorted(dic_socore.items(), key = lambda x: (-x[1], -x[0]))
    print(f'#{i} {answer[0][0]}')

