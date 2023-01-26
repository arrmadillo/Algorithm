import sys
c = int(sys.stdin.readline().rstrip())
nums = []
delete = []
for i in range(c):
    t = int(sys.stdin.readline())
    if t == 0:
        nums.pop()
    else:
        nums.append(t)
print(sum(nums))









