import sys

answer = []
for _ in range(4):
    out_num, in_num = map(int, sys.stdin.readline().rstrip().split())
    if not answer: #빈 리스트인 경우
        answer.append(in_num - out_num)
    else:
        answer.append(answer[-1] - out_num + in_num)
print(max(answer))


