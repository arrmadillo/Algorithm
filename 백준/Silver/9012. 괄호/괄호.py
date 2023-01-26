import sys

t = int(sys.stdin.readline())
a, b = 0, 0
for i in range(t):
    vps = sys.stdin.readline().rstrip()
    if len(vps) % 2 != 0:
        print('NO')
    elif vps.count('(') != vps.count(')'):
        print('NO')
    else:
        for i in vps:
            if a >= b:
                if i == '(':
                    a += 1
                else:
                    b += 1
            else:
                print('NO')
                a, b = 0, 0
                break
        else:
            print('YES')