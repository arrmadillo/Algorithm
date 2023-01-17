nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))
nums3 = list(map(int, input().split()))
sum_nums = [nums1, nums2, nums3]

index0 = 0
index1 = 0
temp0 = []
temp1 = []
for nums in sum_nums:
    temp0.append(nums[0])
    temp1.append(nums[1])
print(min(temp0, key=temp0.count), min(temp1, key=temp1.count))