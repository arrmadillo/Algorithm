score = []
for i in range(5):
    a = int(input())
    if a < 40:
        a = 40
        score.append(a)
    else:
        score.append(a)

print(sum(score) // len(score))