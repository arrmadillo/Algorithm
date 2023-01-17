N = int(input())
nums = [int(input()) for i in range(N)]
nums.sort()
print(*nums, sep='\n')