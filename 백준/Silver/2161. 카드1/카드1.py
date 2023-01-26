import sys
t = int(sys.stdin.readline().rstrip())
nums = [i for i in range(1,t+1)]
answer = []
while(len(nums) > 1):
    answer.append(nums.pop(0))
    change_num = nums.pop(0)
    nums.append(change_num)
print(*answer, *nums)










