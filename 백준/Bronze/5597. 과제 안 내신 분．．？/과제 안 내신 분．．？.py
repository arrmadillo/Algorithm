import sys

students = set([int(sys.stdin.readline()) for i in range(28)])

nums = set([i for i in range(1,31)])

print(*sorted(nums - students), sep='\n')





