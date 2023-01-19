import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
num = str(a*b*c)
count = {i:0 for i in range(10)}
for i in num:
    count[int(i)] += 1
    
for i in range(10):
    print(count[i])