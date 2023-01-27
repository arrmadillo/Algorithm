import sys

status = sys.stdin.readline().rstrip()
stack = []

if status == '고무오리 디버깅 시작':
    while status != '고무오리 디버깅 끝':
        command = sys.stdin.readline().rstrip()
        if command == '문제':
            stack.append(command)
        elif command == '고무오리':
            if stack:
                stack.pop()
            else:
                stack.extend(['문제', '문제'])
        elif not stack:
            print('고무오리야 사랑해')
            status = command
        else:
            print('힝구')
            status = command

