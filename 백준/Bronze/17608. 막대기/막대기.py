import sys

T = int(sys.stdin.readline())

cnt = 0
nums = []

for _ in range(T):
    num = int(sys.stdin.readline())
    nums.append(num)

nums = nums[::-1]
temp = 0

for num in nums:
    if temp < num:
        temp = num
        cnt += 1

print(cnt)