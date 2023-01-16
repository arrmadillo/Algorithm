N = int(input())
result = list(map(int, input().split()))
get_score = 1
score = 0

for i in result:
    if i == 1:
        score += get_score
        get_score += 1
    else:
        get_score = 1
print(score)