

text = input()
answer = []

for _ in text:
    answer.append(ord(_)-64)

print(*answer)

