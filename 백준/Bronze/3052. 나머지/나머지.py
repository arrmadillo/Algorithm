import sys

nums = []

for i in range(10):
    num = int(sys.stdin.readline()) % 42
    nums.append(num)

print(len(set(nums))) 



