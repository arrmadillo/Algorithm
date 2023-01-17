nums = [int(input()) for i in range(9)]
max_num = max(nums)
index = nums.index(max_num)
print(max_num, index+1, sep='\n')