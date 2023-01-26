import sys

nums = [int(sys.stdin.readline()) for i in range(3)]
count = 1

if sum(nums) != 180:
    print('Error')
else:
    for i in nums[0:2]:
        if count < nums.count(i):
            count = nums.count(i)
    if count == 3:
        print('Equilateral')
    elif count == 2:
        print('Isosceles')
    else:
        print('Scalene')