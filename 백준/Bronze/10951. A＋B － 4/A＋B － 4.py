import sys

is_true = True
while(is_true == True):
    try:
        a, b = map(int, sys.stdin.readline().split())
        print(a+b)
    except:
        is_true = False






