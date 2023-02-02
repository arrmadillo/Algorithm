import sys

input = sys.stdin.readline()
case = int(input)
nums = list(map(int,sys.stdin.readline().split()))

first = 0
last = 0
answer = []

for num in nums:
    if first == 0 and last == 0:
        first = num
        last = num
    elif last >= num:
        answer.append(last - first)
        first = num
        last = num
    elif last < num:
        last = num
    
else:
    answer.append(last - first)

print(max(answer))