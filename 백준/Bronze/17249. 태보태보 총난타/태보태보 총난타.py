import sys

punch = sys.stdin.readline().rstrip()
punch = punch.split("(^0^)")
left = 0
right = 0

for i in punch[0]:
    if i == '@':
        left += 1
for i in punch[1]:
    if i == '@':
        right += 1

print(left, right)


