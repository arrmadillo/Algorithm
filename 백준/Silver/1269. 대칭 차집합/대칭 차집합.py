import sys

case = sys.stdin.readline().rstrip()

nums1 = set(map(int, sys.stdin.readline().split()))
nums2 = set(map(int, sys.stdin.readline().split()))

answer = 0
answer += len(nums1-nums2) + len(nums2 - nums1) 
print(answer)



