case = int(input())

answer = list(map(int, input().split()))
middle_i = case // 2 + 1

answer = sorted(answer)

print(answer[middle_i-1])

