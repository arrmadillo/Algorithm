import sys

nums = [int(sys.stdin.readline()) % 42 for i in range(10)]
result = []
for i in nums:
    if i not in result:
        result.append(i)
print(len(result))





