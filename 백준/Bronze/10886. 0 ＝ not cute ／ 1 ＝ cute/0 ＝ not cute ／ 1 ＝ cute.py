N = int(input())
nums = []
for i in range(N):
    nums.append(int(input()))

if max(nums, key=lambda x: nums.count(x)) == 1:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")