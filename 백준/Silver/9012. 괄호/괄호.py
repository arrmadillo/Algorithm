import sys

t = int(sys.stdin.readline())

for i in range(t):
    vps = sys.stdin.readline().rstrip()
    if len(vps) % 2 != 0 or vps.count('(') != vps.count(')'): # 총길이는 항상 짝수, 그리고 짝이 맞아야함
        print('NO')
    else:
        stack = []
        for i in vps:
            if i == '(':
                stack.append(i)
            elif stack:
                stack.pop()
            else:
                print('NO')
                break
        else:
            print('YES')