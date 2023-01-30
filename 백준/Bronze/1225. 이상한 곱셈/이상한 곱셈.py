import sys

num1, num2 = sys.stdin.readline().rstrip().split()

sum_num = 0
answer = 0

for i in range(len(num1)):
    sum_num += int(num1[i])

for j in range(len(num2)):
    answer += sum_num * int(num2[j])

print(answer)