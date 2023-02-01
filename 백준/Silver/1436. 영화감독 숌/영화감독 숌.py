import sys
#
num = int(sys.stdin.readline())
count = 0 #666이 포함될때 카운트
six = '666'
base = 666

while True:
    #양쪽을 바꾸면 시간 초과.
    if six in str(base):
        count += 1
    if count == num:
        print(base)
        break
    base += 1
    

    










