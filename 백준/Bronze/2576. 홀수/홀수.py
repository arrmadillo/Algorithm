import sys

nums = [int(sys.stdin.readline()) for i in range(7)]
answer = []

for i in range(len(nums)):    
    if nums[i] % 2 != 0:
        answer.append(nums[i])
if answer != []:
    print(sum(answer), min(answer), sep='\n')
else:
    print(-1)