import sys

status = 1

while status == 1:
    try:
        t = sys.stdin.readline().rstrip()
        if t == '':
            status = 0
        print(t)
    except:
        status = 0








