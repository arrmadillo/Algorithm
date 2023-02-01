import sys

n = int(sys.stdin.readline())

for num in range(n, 3, -1):
    if len(str(num)) == str(num).count('4') + str(num).count('7'):
        print(num)
        break


