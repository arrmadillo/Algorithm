import sys

case = sys.stdin.readline().rstrip()

nums1 = set(sys.stdin.readline().split())
nums2 = set(sys.stdin.readline().split())

print(len(nums1-nums2) + len(nums2 - nums1) )



