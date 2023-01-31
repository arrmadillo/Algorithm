import sys

nums = []
count = {}

for _ in range(10):
    nums.append(int(sys.stdin.readline()))
    
avr = sum(nums) // 10

for i in nums:
    try:
        count[i] += 1
    except:
        count[i] = 1

count = sorted(count.items(), key=lambda x: -x[1])

print(avr)
print(count[0][0])